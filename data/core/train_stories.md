## retrain_story_1
* greetings
    - received_greet
* command{"action": "grab", "object_color": "blue", "object_name": "bottle"}
    - received_command
* affirmative
    - received_command_confirmed
    - execute_command
* train
    - received_train


## retrain_story_2
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
* train
    - received_train

## retrain_story_3
* greetings
    - received_greet
* train
    - received_train

## retrain_story_4
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
* train
    - received_train

## retrain_story_5
- clarification_form
- form{"name": "clarification_form"}
- form{"name": null}
- utter_clarification_repeat
* train
    - received_train