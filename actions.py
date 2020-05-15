# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import logging
import time
from typing import Any, Dict, List, Text, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset, SlotSet, ActionExecuted, EventType, FollowupAction, Restarted, SessionStarted, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import Action, FormAction, REQUESTED_SLOT
from rasa.core.slots import Slot

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
list_of_synonym    = ['show']

invalid_values = [None, "none", "None", "unknown", "", "any"]



def check_slots_for_command(tracker, dispatcher, action=None, check_confirm=True):
    if action is None:
        action = tracker.get_slot('action')
    object_name = tracker.get_slot('object_name')
    object_color = tracker.get_slot('object_color')
    placement_origin = tracker.get_slot('placement_origin')
    placement_destination = tracker.get_slot('placement_destination')
    command_confirmed = tracker.get_slot('command_confirmed')

    # slots contain a valid command
    if (action not in invalid_values) and (action in list_of_synonym) and (object_name not in invalid_values):

        if (action in ['find', 'pick up']) and placement_destination not in invalid_values and placement_origin in invalid_values:
            placement_origin = placement_destination

        if command_confirmed or not check_confirm:
            return True
        else:
            description = '{} {}'.format(object_color, object_name) if object_color not in invalid_values else object_name
            placement_from = ' {} the {}'.format("in" if placement_origin == "middle" else "on",
                                            placement_origin) if placement_origin not in invalid_values else ' somewhere on the platform'
            placement_to = ' {} the {}'.format("to", placement_destination) if placement_destination not in invalid_values else ' somewhere on the platform'
            if action in ['find', 'pick up']:
                placement = placement_from
            else:
                placement = '{} {}'.format(placement_from, placement_to)
            print(description, placement)
            dispatcher.utter_message(template="utter_repeat_command",
                                     action=action,
                                     object_description=description,
                                     placement=placement)

    # object name given without an action
    elif (action in invalid_values) and (object_name not in invalid_values):
        dispatcher.utter_message(template="utter_prompt_action",
                                 object_name=object_name)

    # action given without an object name
    elif (action not in invalid_values) and (object_name in invalid_values):
        dispatcher.utter_message(template="utter_prompt_object",
                                 action=action)

    # unknown action and object
    elif (action in invalid_values) and (object_name in invalid_values):
        dispatcher.utter_message(template="utter_prompt")

    elif action not in list_of_synonym:
        # logger.warning('unknown actions')
        dispatcher.utter_message(template="utter_unknown_action",
                                 action=action)
        return [FollowupAction("clarification_form")]

    return False


class UserUttered(Action):
    """Fills the action slot when a message is received."""

    def name(self) -> Text: return "user_uttered"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global list_of_synonym
        # dispatcher.utter_message(template="utter_received_command")
        action = tracker.latest_message['intent'].get('name')

        return [SlotSet("action", action)]

class ActionSessionStart(Action):

    """Applies a conversation session start.
    Takes all `SlotSet` events from the previous session and applies them to the new
    session.
    """

    def name(self) -> Text: return "action_session_start"

    @staticmethod
    def _slot_set_events_from_tracker(
        tracker: Tracker,
    ) -> List["SlotSet"]:
        """Fetch SlotSet events from tracker and carry over key, value and metadata."""

        #from rasa.core.events import SlotSet

        return [
            SlotSet(key=event.key, value=event.value, metadata=event.metadata)
            for event in tracker.applied_events()
            if isinstance(event, SlotSet)
        ]

    async def run(
        self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[EventType]:

        global list_of_synonym
        _events = [SessionStarted()]
        _events.extend(self._slot_set_events_from_tracker(tracker))
        _events.append(ActionExecuted("action_listen"))

        list_of_synonym += collect_synonym(input_nlu_file) + collect_synonym(user_nlu_file)  # fill the list of known actions from training file

        return _events

class ReceivedFind(Action):
    def name(self) -> Text: return "execute_find"

    def run(self, dispatcher, tracker, domain):

        object_name = tracker.get_slot('object_name')
        object_color = tracker.get_slot('object_color')
        placement_origin = tracker.get_slot('placement')
        if ENABLE_ROS:
            nlp_node.send_command("show", object_name, object_color, placement_origin)
            response, info = nlp_node.wait_for_response()

            if response is not None:
                dispatcher.utter_message(template="utter_executed_command")

                imgpath = info
                print("Image saved at {}".format(imgpath))
                print("Found {} object: {}".format(response.desired_color, response.found_obj))

                imgurl = "http://localhost:8888/{}?time={}".format(imgpath, int(time.time()))
                dispatcher.utter_attachment(None, image=imgurl)

                placement = ' in the {} area of the platform'.format(placement_origin) if placement_origin not in invalid_values else ''

                if response.found_obj and response.desired_color not in invalid_values:
                    dispatcher.utter_message(text="I found the {} object you asked for{}.".format(response.desired_color, placement))
                elif response.found_obj and response.desired_color in invalid_values:
                    dispatcher.utter_message(text="You didn't specify any color, but here are the objects I found{}.".format(placement))
                elif not response.found_obj and response.desired_color not in invalid_values:
                    dispatcher.utter_message(text="Sorry, I didn't find any {} object{}.".format(response.desired_color, placement))
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


class ReceivedCommandConfirmed(Action):

    def name(self) -> Text: return "received_command_confirmed"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if check_slots_for_command(tracker, dispatcher, check_confirm=False):
            dispatcher.utter_message(template="utter_got_confirmation")

        return [
            SlotSet("command_confirmed", True)
        ]


class ReceivedCancel(Action):
    """Reset all slots if a command was denied."""

    def name(self) -> Text: return "cancel_command"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        return [AllSlotsReset()]
