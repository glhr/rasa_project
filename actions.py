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

    def name(self) -> Text: return "got_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # dispatcher.utter_message(template="utter_received_command")
        action = tracker.latest_message['intent'].get('name')
        logger.info('Got action: {}'.format(action))

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
        if ENABLE_ROS:
            nlp_node.send_command("find", object_name, object_color, placement_origin)
            response, info = nlp_node.wait_for_response()

            if response is not None:
                dispatcher.utter_message(template="utter_executed_command")

                imgpath = info
                print("Image saved at {}".format(imgpath))
                print("Found {} object: {}".format(response.desired_color, response.found_obj))

                imgurl = "http://localhost:8888/{}?time={}".format(imgpath, int(time.time()))
                dispatcher.utter_attachment(None, image=imgurl)

                if response.found_obj:
                    dispatcher.utter_message(text="I found the {} object you asked for on the {}.".format(
                        response.desired_color,
                        placement_origin
                        ))
                # elif response.found_obj and response.desired_color in invalid_values:
                #     dispatcher.utter_message(text="You didn't specify any color, but here are the objects I found{}.".format(placement))
                # elif not response.found_obj and response.desired_color not in invalid_values:
                #     dispatcher.utter_message(text="Sorry, I didn't find any {} object{}.".format(response.desired_color, placement))
                else:
                    dispatcher.utter_message(text="This is what I can see.")
            else:
                dispatcher.utter_message(template="utter_failed_command")
                dispatcher.utter_message(text="Error: {}...Check that the required ROS Service is running!".format(info))


class ReceivedLearn(Action):
    def name(self) -> Text: return "execute_learn"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        object_name = tracker.get_slot('object_name')
        object_color = tracker.get_slot('object_color')
        placement = tracker.get_slot('placement')

        if ENABLE_ROS:
            nlp_node.send_command(action="show",
                                  object=object_name,
                                  obj_color=object_color,
                                  placement_origin="middle",
                                  placement_destination=None)

            response, info = nlp_node.wait_for_response()

            if response is not None:
                imgpath = info
                print("Image saved at {}".format(imgpath))
                print("Found object: {}".format(response.desired_color, response.found_obj))

                imgurl = "http://localhost:8888/{}?time={}".format(imgpath,int(time.time()))
                dispatcher.utter_attachment(None, image=imgurl)

                if response.found_obj:
                    dispatcher.utter_message(text="This is the object I found in the middle of the platform.".format(response.desired_color))
                    dispatcher.utter_message(template="utter_got_description")
                else:
                    dispatcher.utter_message(text="Sorry, I didn't find any object. Make sure the object you want to show me is in the middle of the platform.".format(response.desired_color))
            else:
                dispatcher.utter_message(template="utter_failed_command")
                dispatcher.utter_message(text="Error: {}".format(info))

            return [AllSlotsReset()]
        return []



class ReceivedCancel(Action):
    """Reset all slots if a command was denied."""

    def name(self) -> Text: return "cancel_command"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [AllSlotsReset()]
