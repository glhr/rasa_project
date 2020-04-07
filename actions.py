# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

import logging
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import Restarted, SessionStarted, ActionExecuted, EventType
from rasa_sdk.executor import CollectingDispatcher

from synonym_extraction import collect_synonym, add_synonym

logger = logging.getLogger(__name__)

try:
    from ros_comm import nlp_node
    ENABLE_ROS = True
except Exception as e:
    logger.warning("Failed to load ros_comm module: {}".format(e))
    ENABLE_ROS = False

input_nlu_file = './data/nlu.md'
user_nlu_file = './data/user_nlu.md'
list_of_syn = []


class ActionSessionStart(Action):

    """Applies a conversation session start.
    Takes all `SlotSet` events from the previous session and applies them to the new
    session.
    """

    def name(self) -> Text:
        return "action_session_start"

    @staticmethod
    def _slot_set_events_from_tracker(
        tracker: Tracker,
    ) -> List["SlotSet"]:
        """Fetch SlotSet events from tracker and carry over key, value and metadata."""

        from rasa.core.events import SlotSet

        return [
            SlotSet(key=event.key, value=event.value, metadata=event.metadata)
            for event in tracker.applied_events()
            if isinstance(event, SlotSet)
        ]

    async def run(
        self, dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[EventType]:

        global list_of_syn
        _events = [SessionStarted()]
        _events.extend(self._slot_set_events_from_tracker(tracker))
        _events.append(ActionExecuted("action_listen"))

        list_of_syn = collect_synonym(input_nlu_file) + collect_synonym(user_nlu_file)  # fill the list of known actions from training file

        return _events


class ReceivedCommand(Action):

    def name(self) -> Text: return "received_command"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        global list_of_syn
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

            if action in list_of_syn:
                #logger.warning('known actions')
                dispatcher.utter_message(template="utter_repeat_command",
                                     action=action,
                                     object_color=object_color,
                                     object_name=object_name)
            else:
                #logger.warning('unknown actions')
                dispatcher.utter_message(template="utter_unknown_action_command",
                                     action=action)
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
        image_url="https://i.kym-cdn.com/entries/icons/facebook/000/002/691/sings.jpg"
        dispatcher.utter_attachment(None, image=image_url)

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
