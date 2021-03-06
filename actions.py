# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import logging
import time
from typing import Any, Dict, List, Text, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset, UserUttered, SlotSet, ActionExecuted, EventType, FollowupAction, Restarted, SessionStarted, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import Action, FormAction, REQUESTED_SLOT
from rasa.core.slots import Slot
from rasa.core.events import Event

from synonym_extraction import collect_synonym, add_synonym
from slots import valid_placements, update_known_colors, update_known_objects

from train import train_model

logger = logging.getLogger(__name__)

try:
    from ros_comm import nlp_node
    ENABLE_ROS = True
except Exception as e:
    logger.warning("Failed to load ros_comm module: {}".format(e))
    ENABLE_ROS = False

input_nlu_file = './data/nlu.md'
user_nlu_file  = './data/user_nlu.md'
input_nlu_file = './data/nlu/synonyms.md'
user_nlu_file  = './data/nlu/user_nlu.md'



class FillActionSlot(Action):
    """Fills the action slot when a message is received."""

    def name(self) -> Text: return "action_fill"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(template="utter_received_command")
        action = tracker.latest_message['intent'].get('name')
        logger.info('Got action: {}'.format(action))

        logger.debug(tracker.sender_id)
        if action in ['find', 'pick up', 'move']:
            return [SlotSet("action", action)]
        elif action == 'show':
            return [SlotSet("action", "learn")]
        else:
            return []



class ReceivedFind(Action):
    def name(self) -> Text: return "execute_find"

    def run(self, dispatcher, tracker, domain):

        object_name = tracker.get_slot('object_name')
        object_color = tracker.get_slot('object_color')
        placement_origin = tracker.get_slot('placement')
        #
        # if placement_origin not in valid_placements:
        #     placement_origin = "any"
        #     dispatcher.utter_message(text="Hang on, I'll try to find a {} {} somewhere on the table".format(
        #         object_color,
        #         object_name
        #     ))
        # else:
        #     dispatcher.utter_message(text="Hang on, I'll try to find a {} {} in the {} area of the table".format(
        #         object_color,
        #         object_name,
        #         placement_origin
        #     ))

        if ENABLE_ROS:
            nlp_node.send_command("find", object_name, object_color, placement_origin)
            response = nlp_node.wait_for_response()
            try:
                msg, path_2dimg, path_3dimg = response
            except Exception:
                msg, path_2dimg = response

            if msg is not None:
                # dispatcher.utter_message(template="utter_executed_command")

                # handle 2d vision response
                print("Found {} object: {}".format(msg.desired_color, msg.found_obj))

                imgurl_2d = "http://localhost:8888/{}?time={}".format(path_2dimg, int(time.time()))
                dispatcher.utter_attachment(None, image=imgurl_2d)

                if msg.found_obj:
                    if placement_origin in valid_placements:
                        dispatcher.utter_message(text="I found the {} object you asked for in the {} area.".format(
                            msg.desired_color,
                            placement_origin
                            ))
                    else:
                        dispatcher.utter_message(text="I found the {} object you asked for.".format(
                            msg.desired_color
                            ))
                else:
                    if placement_origin in valid_placements:
                        dispatcher.utter_message(text="I didn't find anything {} in the {} area. This is what I can see".format(
                            msg.desired_color,
                            placement_origin
                            ))
                    else:
                        dispatcher.utter_message(text="I didn't find anything {}. This is what I can see.".format(
                            msg.desired_color
                            ))

                # handle 3D Vision response

                try:
                    imgurl_3d = "http://localhost:8888/{}?time={}".format(path_3dimg, int(time.time()))
                    if msg.pcl_obj:
                        dispatcher.utter_attachment(None, image=imgurl_3d)
                        dispatcher.utter_message(text="I found the {} you asked for.".format(
                            msg.pcl_object
                            ))
                    # else:
                    #     dispatcher.utter_message(text="I didn't find any {}.".format(
                    #         object_name
                    #         ))
                except Exception as e:
                    logger.warning(e)
            else:
                dispatcher.utter_message(template="utter_command_failed")
                return [AllSlotsReset()]
                # dispatcher.utter_message(text="Error: {}...Check that the required ROS Service is running!".format(info))
        else:
            dispatcher.utter_message(text="I found the {} {} you asked for.".format(
                object_color,
                object_name
                ))
        return [AllSlotsReset()]


class ReceivedLearn(Action):
    def name(self) -> Text: return "execute_learn"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        object_name = tracker.get_slot('object_name')
        object_color = tracker.get_slot('object_color')
        placement = tracker.get_slot('placement')

        if placement in valid_placements:
            placement_origin = placement
        else:
            placement_origin="middle"
        #
        # dispatcher.utter_message(text="Hang on, I'll try to search in the {} area of the table for the object you want me to learn".format(
        #     placement_origin
        # ))

        if ENABLE_ROS:
            nlp_node.send_command(action="show",
                                  object=object_name,
                                  obj_color=object_color,
                                  placement_origin=placement_origin,
                                  placement_destination=None)

            response = nlp_node.wait_for_response()
            try:
                msg, path_2dimg, path_3dimg = response
            except Exception:
                msg, path_2dimg = response

            if msg is not None:
                imgpath = path_2dimg
                print("Image saved at {}".format(imgpath))
                print("Found object: {}".format(msg.desired_color, msg.found_obj))

                imgurl = "http://localhost:8888/{}?time={}".format(imgpath,int(time.time()))
                dispatcher.utter_attachment(None, image=imgurl)

                if msg.found_obj:
                    # dispatcher.utter_message(text="I found the {} {} in the {} area of the platform.".format(
                    #     msg.desired_color,
                    #     object_name,
                    #     placement_origin))
                    dispatcher.utter_message(template="utter_got_description")
                    update_known_objects([object_name])
                    update_known_colors([object_color])
                else:
                    dispatcher.utter_message(text="Sorry, I didn't find any object. Make sure the {} {} you want to show me is in the {} area of the platform.".format(
                        msg.desired_color,
                        object_name,
                        placement_origin))
            else:
                dispatcher.utter_message(template="utter_command_failed")
                # dispatcher.utter_message(text="Error: {}".format(info))

            return [AllSlotsReset()]
        else:
            dispatcher.utter_message(template="utter_got_description")
        return [AllSlotsReset()]


class ReceivedPickup(Action):
    def name(self) -> Text: return "execute_pickup"

    def run(self, dispatcher, tracker, domain):

        object_name = tracker.get_slot('object_name')
        object_color = tracker.get_slot('object_color')
        placement_origin = tracker.get_slot('placement')

        # if placement_origin not in valid_placements:
        #     placement_origin = "any"
        #     dispatcher.utter_message(text="Hang on, I'll try to pick up the {} {} somewhere on the table".format(
        #         object_color,
        #         object_name
        #     ))
        # else:
        #     dispatcher.utter_message(text="Hang on, I'll try to pick up the {} {} in the {} area of the table".format(
        #         object_color,
        #         object_name,
        #         placement_origin
        #     ))

        if ENABLE_ROS:
            nlp_node.send_command("pick up", object_name, object_color, placement_origin)
            response = nlp_node.wait_for_response()
            try:
                msg, path_2dimg, _ = response
            except Exception:
                msg, path_2dimg = response

            if msg is not None:
                # dispatcher.utter_message(template="utter_executed_command")
                if path_2dimg is not None:
                    imgpath = path_2dimg
                    print("Image saved at {}".format(imgpath))
                    print("Found {} object: {}".format(msg.desired_color, msg.found_obj))
                    imgurl = "http://localhost:8888/{}?time={}".format(imgpath, int(time.time()))
                    dispatcher.utter_attachment(None, image=imgurl)

                # dispatcher.utter_message(text="Got response code {} from gripper.".format(msg.grippercode))
                if msg.grippercode in [1,2,3]:
                    dispatcher.utter_message(template="utter_command_failed")
                else:
                    dispatcher.utter_message(text="I've managed to pick it up!")
            else:
                dispatcher.utter_message(template="utter_command_failed")
                return [AllSlotsReset()]
                # dispatcher.utter_message(text="Error: {}...Check that the required ROS Service is running!".format(info))
        else:
            dispatcher.utter_message(text="I've managed to pick it up!")
        return [AllSlotsReset()]


class ReceivedMove(Action):
    def name(self) -> Text: return "execute_move"

    def run(self, dispatcher, tracker, domain):

        object_name = tracker.get_slot('object_name')
        object_color = tracker.get_slot('object_color')
        placement_destination = tracker.get_slot('placement')
        #
        # dispatcher.utter_message(text="Hang on, I'll try to move the {} {} to the {}".format(
        #     object_color,
        #     object_name,
        #     placement_destination
        # ))

        if ENABLE_ROS:
            nlp_node.send_command("move", object_name, object_color, placement_destination=placement_destination, placement_origin="any")
            response = nlp_node.wait_for_response()
            try:
                msg, path_2dimg, _ = response
            except Exception:
                msg, path_2dimg = response

            if msg is not None:
                # dispatcher.utter_message(template="utter_executed_command")
                if path_2dimg is not None:
                    imgpath = path_2dimg
                    print("Image saved at {}".format(imgpath))
                    print("Found {} object: {}".format(msg.desired_color, msg.found_obj))
                    imgurl = "http://localhost:8888/{}?time={}".format(imgpath, int(time.time()))
                    dispatcher.utter_attachment(None, image=imgurl)

                # dispatcher.utter_message(text="Got response code {} from gripper.".format(msg.grippercode))
                if msg.grippercode in [1,2,3]:
                    dispatcher.utter_message(template="utter_command_failed")
                else:
                    dispatcher.utter_message(text="I've managed to move it!")
            else:
                dispatcher.utter_message(template="utter_command_failed")
                return [AllSlotsReset()]
                # dispatcher.utter_message(text="Error: {}...Check that the required ROS Service is running!".format(info))
        else:
            dispatcher.utter_message(text="I've managed to move it!")
        return [AllSlotsReset()]

class ReceivedCancel(Action):
    """Reset all slots if a command was denied."""

    def name(self) -> Text: return "action_cancel"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [AllSlotsReset()]


class FallbackAction(Action):
    """This action is triggered in case of uncertain/ambiguous predictions."""

    def name(self) -> Text: return "action_fallback"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="Sorry, I'm not that smart yet so I'm not sure what you want me to do. I can find an object, pick it up, or move it to a certain location.")

        return []


class RetrainAction(Action):
    """This action is triggered in case of uncertain/ambiguous predictions."""

    def name(self) -> Text: return "action_retrain"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(
            text="Re-training model")

        train_model()

        return []
