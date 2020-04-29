# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import logging
import time
from typing import Any, Dict, List, Text, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.events import ActionExecuted, EventType, FollowupAction, Restarted, SessionStarted, SlotSet
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
list_of_synonym    = []


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

        list_of_synonym = collect_synonym(input_nlu_file) + collect_synonym(user_nlu_file)  # fill the list of known actions from training file

        return _events


class ReceivedCommand(Action):

    def name(self) -> Text: return "received_command"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global list_of_synonym
        # dispatcher.utter_message(template="utter_received_command")
        action = next(tracker.get_latest_entity_values("action"), None)
        object_color = next(tracker.get_latest_entity_values("object_color"), None)
        object_name = next(tracker.get_latest_entity_values("object_name"), None)
        placement_origin = next(tracker.get_latest_entity_values("placement_origin"), None)
        placement_destination = next(tracker.get_latest_entity_values("placement_destination"), None)

        if ENABLE_ROS:
            nlp_node.send_raw_msg(tracker.latest_message['text'])

        if (action is not None) and (object_name is not None):
            if object_color is None: object_color = ''

            if action in list_of_synonym:
                #logger.warning('known actions')
                dispatcher.utter_message(template="utter_repeat_command",
                                     action=action,
                                     object_color=object_color,
                                     object_name=object_name)
            else:
                #logger.warning('unknown actions')
                dispatcher.utter_message(template="utter_unknown_action_command",
                                     action=action)
                return [FollowupAction("clarification_form")]
                
        elif (action is None) and (object_name is not None):
            dispatcher.utter_message(template="utter_incomplete_command_missing_action",
                                     object_name=object_name)
        
        elif (action is not None) and (object_name is None):
            dispatcher.utter_message(template="utter_incomplete_command_missing_object",
                                     action=action)

        return []


class ReceivedCommandConfirmed(Action):

    def name(self) -> Text: return "received_command_confirmed"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_user_gave_confirmation")

        return []


class ExecuteCommand(Action):

    def name(self) -> Text: return "execute_command"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        action = tracker.get_slot('action')
        logger.info(action)
        logger.info(tracker.slots)
        object_name = tracker.get_slot('object_name')
        object_color = tracker.get_slot('object_color')
        placement_origin = tracker.get_slot('placement_origin')
        placement_destination = tracker.get_slot('placement_destination')

        if ENABLE_ROS:
            nlp_node.send_raw_msg(tracker.latest_message['text'])
            nlp_node.send_command(action, object_name, object_color, placement_origin, placement_destination)
            if action == "find":
                response, imgpath = nlp_node.wait_for_response()

                if response is not None:
                    dispatcher.utter_message(template="utter_executed_command")
                    print("Image saved at {}".format(imgpath))
                    print("Found {} object: {}".format(response.desired_color, response.found_obj))

                    imgurl = "http://localhost:8888/{}?time={}".format(imgpath,int(time.time()))
                    dispatcher.utter_attachment(None, image=imgurl)

                    if response.found_obj:
                        dispatcher.utter_message(text="I found the {} object you asked for.".format(response.desired_color))
                    else:
                        dispatcher.utter_message(text="Sorry, I didn't find any {} object.".format(response.desired_color))
                else:
                    dispatcher.utter_message(template="utter_failed_command")

        return []

class ReceivedCommandDenied(Action):

    def name(self) -> Text: return "received_command_denied"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if ENABLE_ROS:
            nlp_node.send_raw_msg(tracker.latest_message['text'])

        dispatcher.utter_message(template="utter_user_denied")
        return []


class ReceivedGoodbye(Action):

    def name(self) -> Text: return "received_goodbye"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if ENABLE_ROS:
            nlp_node.send_raw_msg(tracker.latest_message['text'])

        dispatcher.utter_message(template="utter_goodbye")
        return []

class ReceivedNone(Action):

    def name(self) -> Text: return "received_none"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if ENABLE_ROS:
            nlp_node.send_raw_msg(tracker.latest_message['text'])

        dispatcher.utter_message(template="utter_prompt")
        return []

class ReceivedGreet(Action):

    def name(self) -> Text: return "received_greet"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if ENABLE_ROS:
            nlp_node.send_raw_msg(tracker.latest_message['text'])

        dispatcher.utter_message(template="utter_greet")
        return []

class ReceivedRestart(Action):

    def name(self) -> Text: return "received_restart"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        if ENABLE_ROS:
            nlp_node.send_raw_msg(tracker.latest_message['text'])

        dispatcher.utter_message(template="utter_restart")
        def apply_to(self, tracker) -> None:
            tracker._reset_slots()
        return[Restarted()]

class ActionClarificationForm(FormAction):

    def name(self) -> Text: return "clarification_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["synonym_category"]

    @staticmethod
    def synonym_db() -> List[Text]:
        """Database of supported categories for synonyms"""

        return [
            "find",
            "move",
            "pick up"
        ]

    def slot_mappings(self):
        return {
            "synonym_category": self.from_entity(entity="synonym_category", intent=["inform", "new_synonym_add"])}

    def validate_synonym(self, value: Text, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> Dict[Text, Any]:
        """Validate synonym category value."""

        slot_values = self.extract_other_slots(dispatcher, tracker, domain)
        
        if value.lower() in self.synonym_db():
            # validation succeeded, set the value of the "synonym category" slot to value
            return [SlotSet('synonym_category', value)]
        else:
            dispatcher.utter_message(template="utter_wrong_synonym_category")
            # validation failed, set this slot to None, meaning the user will be asked for the slot again
            return [SlotSet('synonym_category', None)]

    def submit(self, dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict]:

        action = tracker.get_slot('action')
        synonym_category = tracker.get_slot('synonym_category')

        """Define what the form has to do after all required slots are filled"""
        add_synonym(synonym_category, action)       # saves the new action as a synonym for the specific category
        #print(synonym_category, action)

        dispatcher.utter_message(template="utter_clarification_repeat")
        return []

        