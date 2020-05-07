## interactive_story_1
* show{"object_color": "purple", "object_name": "cherry"}
    - received_show
* affirmative
    - received_show_confirmed
    - execute_command
* greetings
    - utter_greet
* command{"action": "pick up", "object_color": "yellow", "object_name": "ball"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* show
    - received_show
* bye
    - utter_goodbye

## interactive_story_1
* greetings
    - utter_greet
* command{"action": "grab", "object_color": "blue", "object_name": "bottle"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* bye
    - utter_goodbye

## interactive_story_1
* greetings
    - utter_greet
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
    - utter_goodbye

## interactive_story_1
* greetings
    - utter_greet
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
    - utter_goodbye

## interactive_story_1
* greetings
    - utter_greet
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
    - utter_goodbye

## interactive_story_1
* greetings
    - utter_greet
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
    - utter_goodbye

## interactive_story_1
* greetings
    - utter_greet
* bye
    - utter_goodbye
* greetings
    - utter_greet
* command{"action": "pick up", "object_color": "gold", "object_name": "phone"}
    - received_command
* deny
    - received_command_denied
* bye
    - utter_goodbye

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


## interactive_story_1
* greetings
    - utter_greet
* none
    - utter_prompt
* command{"action": "find", "object_color": "red", "object_name": "ball", "placement_destination": "left"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* none
    - utter_prompt
* bye
    - utter_goodbye

## interactive_story_1
* greetings
    - utter_greet
* none
    - utter_prompt
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
    - utter_prompt
* bye
    - utter_goodbye

## interactive_story_1
* greetings
    - utter_greet
* show{"undefined_object": "thing", "object_name": "watermelon"}
    - received_show
* deny
    - received_command_denied
* none
    - utter_prompt
* command{"action": "find", "undefined_object": "something"}
    - received_command
* command{"action": "find", "object_color": "red", "object_name": "apple"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* none
    - utter_prompt
* command{"action": "push", "object_name": "apple"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command

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

## interactive_story_1
* greetings
    - utter_greet
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


## retrain_story_1
* greetings
    - utter_greet
* command{"action": "grab", "object_color": "blue", "object_name": "bottle"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command


## retrain_story_2
* greetings
    - utter_greet
* command{"action": "pick up", "object_name": "waffle"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* command{"action": "detect", "undefined_object": "something", "object_color": "blue"}
    - received_command
* deny
    - received_command_denied

## retrain_story_3
* greetings
    - utter_greet

## retrain_story_4
* show{"object_color": "purple", "object_name": "cherry"}
    - received_show
* affirmative
    - received_show_confirmed
    - execute_command
* greetings
    - utter_greet
* command{"action": "pick up", "object_color": "yellow", "object_name": "ball"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
