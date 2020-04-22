## interactive_story_1
* greetings
    - received_greet
* command{"action": "pick up", "object_color": "yellow", "object_name": "ball"}
    - received_command
* affirmative
    - received_command_confirmed
* bye
    - received_goodbye
* restart
    - action_restart

## interactive_story_1
* greetings
    - received_greet
* command{"action": "grab", "object_color": "blue", "object_name": "bottle"}
    - received_command
* affirmative
    - received_command_confirmed
* bye
    - received_goodbye
* restart
    - action_restart

## interactive_story_1
* greetings
    - received_greet
* command{"action": "pick up", "object_name": "waffle"}
    - received_command
* affirmative
    - received_command_confirmed
* command{"action": "detect", "undefined_object": "something", "object_color": "blue"}
    - received_command
* deny
    - received_command_denied
* bye
    - received_goodbye
* restart
    - action_restart

## interactive_story_1
* greetings
    - received_greet
* command{"action": "detect", "object_color": "red", "object_name": "book"}
    - received_command
* deny{"action": "stop"}
    - received_command_denied
* command{"action": "find", "object_color": "gold", "object_name": "phone"}
    - received_command
* affirmative
    - received_command_confirmed
* command{"action": "lift", "object_name": "phone"}
    - received_command
* affirmative
    - received_command_confirmed
* command{"action": "drop", "undefined_object": "it", "placement": "right"}
    - received_command
* affirmative
    - received_command_confirmed
* bye
    - received_goodbye
* restart
    - action_restart

## interactive_story_1
* greetings
    - received_greet
* command{"action": "move", "object_color": "yellow", "object_name": "cable", "placement": "left"}
    - received_command
* affirmative
    - received_command_confirmed
* command{"action": "recognize", "object_name": "bracelet"}
    - received_command
* deny
    - received_command_denied
* command{"action": "find", "object_name": "bracelet"}
    - received_command
* affirmative
    - received_command_confirmed
* deny
    - received_command_denied
* bye
    - received_goodbye
* restart
    - action_restart

## interactive_story_1
* greetings
    - received_greet
* command{"action": "move", "object_name": "ball", "placement": "right"}
    - received_command
* affirmative
    - received_command_confirmed
* command{"action": "lift", "object_name": "phone"}
    - received_command
* deny
    - received_command_denied
* bye
    - received_goodbye
* restart
    - action_restart

## interactive_story_1
* greetings
    - received_greet
* bye
    - received_goodbye
* greetings
    - received_greet
* command{"action": "pick up", "object_color": "gold", "object_name": "phone"}
    - received_command
* deny
    - received_command_denied
* bye
    - received_goodbye
* restart
    - action_restart

## interactive_story_1
* command{"action": "move", "object_name": "phone"}
    - received_command
* affirmative{"action": "move"}
    - received_command_confirmed
* command{"action": "pick up", "object_name": "apricot"}
    - received_command
* deny
    - received_command_denied
* restart
    - action_restart

## interactive_story_1
* greetings
    - received_greet
* none
    - received_none
* command{"action": "Find", "object_color": "red", "object_name": "ball", "placement_destination": "left"}
    - received_command
* affirmative
    - received_command_confirmed
* none
    - received_none
* bye
    - received_goodbye
* restart
    - action_restart

## interactive_story_1
* greetings
    - received_greet
* none
    - received_none
* command{"action": "pick up", "object_color": "pink", "object_name": "flamingo"}
    - received_command
* affirmative
    - received_command_confirmed
* none
    - received_none
* bye
    - received_goodbye
* restart
    - action_restart

## interactive_story_1
* greetings
    - received_greet
* none
    - received_none
* command{"action": "find", "undefined_object": "something"}
    - received_command
* command{"action": "Find", "object_color": "red", "object_name": "apple"}
    - received_command
* affirmative
    - received_command_confirmed
* none
    - received_none
* command{"action": "push", "object_name": "apple"}
    - received_command
* affirmative
    - received_command_confirmed
* restart
    - action_restart

## interactive_story_1
* command{"action": "move", "object_name": "ball", "placement_origin": "left", "placement_destination": "right"}
    - received_command
* affirmative
    - utter_user_gave_confirmation
* command{"action": "move", "object_name": "ball", "placement_origin": "left", "placement_destination": "right"}
    - received_command
* deny
    - utter_user_denied
* bye
    - utter_goodbye

<!-- ## clarification_form_story_1
* greetings
    - received_greet
* command{"action": null}
* new_synonym_add
    - form{"name": "clarification_form"}
    - form{"name": null}
    - clarification_form
    - utter_clarification_repeat -->

<!-- ## clarification_form_story_2
* form: choose{"synonym_category": "pick up"}
    - slot{"synonym_category": "pick up"}
    - form clarification_form
    - slot{"synonym_category": "pick up"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart

## clarification_form_story_3
* form: choose{"synonym_category": "show"}
    - slot{"synonym_category": "show"}
    - form clarification_form
    - slot{"synonym_category": "show"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart

## clarification_form_story_4
* form: choose{"synonym_category": "move"}
    - slot{"synonym_category": "move"}
    - form clarification_form
    - slot{"synonym_category": "move"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_restart -->

## clarification_story_1
- clarification_form
- form{"name": "clarification_form"}
- form{"name": null}
- utter_clarification_repeat