## interactive_story_1
* greetings
    - received_greet
* command{"action": "pick up", "object_color": "yellow", "object_name": "ball"}
    - received_command
* affirmative
    - received_command_confirmed
* bye
    - received_goodbye

## interactive_story_1
* greetings
    - received_greet
* command{"action": "grab", "object_color": "blue", "object_name": "bottle"}
    - received_command
* affirmative
    - received_command_confirmed
* bye
    - received_goodbye

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
* bye

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
