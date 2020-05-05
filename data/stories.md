## interactive_story_1
* show{"object_color": "purple", "object_name": "cherry"}
    - received_show
* affirmative
    - received_show_confirmed
    - execute_command
* greetings
    - received_greet
* command{"action": "pick up", "object_color": "yellow", "object_name": "ball"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* show
    - received_show
* bye
    - received_goodbye
* restart
    - received_restart

## interactive_story_1
* greetings
    - received_greet
* command{"action": "grab", "object_color": "blue", "object_name": "bottle"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* bye
    - received_goodbye
* restart
    - received_restart

## interactive_story_1
* greetings
    - received_greet
* command{"action": "pick up", "object_name": "waffle"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* command{"action": "detect", "undefined_object": "something", "object_color": "blue"}
    - received_command
* deny
    - received_command_denied
* bye
    - received_goodbye
* restart
    - received_restart

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
    - execute_command
* command{"action": "lift", "object_name": "phone"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* command{"action": "drop", "undefined_object": "it", "placement": "right"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* bye
    - received_goodbye
* restart
    - received_restart

## interactive_story_1
* greetings
    - received_greet
* command{"action": "move", "object_color": "yellow", "object_name": "cable", "placement": "left"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* command{"action": "recognize", "object_name": "bracelet"}
    - received_command
* deny
    - received_command_denied
* command{"action": "find", "object_name": "bracelet"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* deny
    - received_command_denied
* bye
    - received_goodbye
* restart
    - received_restart

## interactive_story_1
* greetings
    - received_greet
* command{"action": "move", "object_name": "ball", "placement": "right"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* command{"action": "lift", "object_name": "phone"}
    - received_command
* deny
    - received_command_denied
* bye
    - received_goodbye
* restart
    - received_restart

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
    - received_restart

## interactive_story_1
* command{"action": "move", "object_name": "phone"}
    - received_command
* affirmative{"action": "move"}
    - received_command_confirmed
    - execute_command
* command{"action": "pick up", "object_name": "apricot"}
    - received_command
* deny
    - received_command_denied
* restart
    - received_restart

## interactive_story_1
* greetings
    - received_greet
* none
    - received_none
* command{"action": "find", "object_color": "red", "object_name": "ball", "placement_destination": "left"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* none
    - received_none
* bye
    - received_goodbye
* restart
    - received_restart

## interactive_story_1
* greetings
    - received_greet
* none
    - received_none
* command{"action": "pick up", "object_color": "pink", "object_name": "flamingo"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* show{"object_name": "grapefruit"}
    - received_show
* affirmative
    - received_show_confirmed
    - execute_command
* none
    - received_none
* bye
    - received_goodbye
* restart
    - received_restart

## interactive_story_1
* greetings
    - received_greet
* show{"undefined_object": "thing", "object_name": "watermelon"}
    - received_show
* deny
    - received_command_denied
* none
    - received_none
* command{"action": "find", "undefined_object": "something"}
    - received_command
* command{"action": "Find", "object_color": "red", "object_name": "apple"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* none
    - received_none
* command{"action": "push", "object_name": "apple"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* restart
    - received_restart

## interactive_story_1
* command{"action": "move", "object_name": "ball", "placement_origin": "left", "placement_destination": "right"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* command{"action": "move", "object_name": "ball", "placement_origin": "left", "placement_destination": "right"}
    - received_command
* deny
    - received_command_denied

## interactive_story_1
* show
    - received_show

## clarification_story_1
- clarification_form
- form{"name": "clarification_form"}
- form{"name": null}
- utter_clarification_repeat

## retrain_story_1
- clarification_form
- form{"name": "clarification_form"}
- form{"name": null}
- utter_clarification_repeat
* train
    - received_train

## retrain_story_2
* greetings
    - received_greet
* command{"action": "grab", "object_color": "blue", "object_name": "bottle"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* train
    - received_train
* bye
    - received_goodbye
* restart
    - received_restart
## interactive_story_1
* greetings
    - received_greet
* show{"object_color": "red", "object_name": "apple"}
    - received_show
* command{"action": "pick", "undefined_object": "it"}
    - received_command
* show{"object_color": "green", "object_name": "kiwi"}
    - received_show
* affirmative
    - received_show_confirmed
    - execute_command
* show{"object_name": "pineapple"}
    - received_show
* deny
    - received_command_denied
