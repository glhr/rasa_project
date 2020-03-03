# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import Restarted
from rasa_sdk.executor import CollectingDispatcher

try:
    from ros_comm import nlp_node
    ENABLE_ROS = True
except:
    ENABLE_ROS = False

class ReceivedCommand(Action):

    def name(self) -> Text: return "received_command"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_received_command")
        action = next(tracker.get_latest_entity_values("action"), None)
        object_color = next(tracker.get_latest_entity_values("object_color"), None)
        object_name = next(tracker.get_latest_entity_values("object_name"), None)

        if ENABLE_ROS:
            nlp_node.send_raw_msg(tracker.latest_message['text'])

        if (action is not None) and (object_name is not None):
            if object_color is None: object_color = ''
            
            if ENABLE_ROS:
                nlp_node.send_command(action,object_name,object_color)

            dispatcher.utter_message(template="utter_repeat_command",
                                     action=action,
                                     object_color=object_color,
                                     object_name=object_name)
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

        if ENABLE_ROS:
            nlp_node.send_raw_msg(tracker.latest_message['text'])

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