
## interactive_story_1
* greetings
    - utter_greet
    - utter_prompt
* show{"object_name": "banana"}
    - utter_prompt_color
* clarify
    - utter_got_description
    - execute_learn

## interactive_story_1
* show{"object_color": "red"}
    - utter_prompt_object
* clarify
    - utter_got_description
    - execute_learn

## interactive_story_1
* show{"object_name": "apple"}
    - slot{"object_name": "apple"}
    - utter_prompt_color
* clarify{"object_color": "green"}
    - slot{"object_color": "green"}
    - utter_got_description
    - execute_learn
* none
    - utter_prompt
* pick up{"object_name": "ball"}
    - slot{"object_name": "ball"}
    - utter_prompt_color
* clarify{"object_color": "blue"}
    - slot{"object_color": "blue"}
    - utter_repeat_command
* affirmative
    - execute_pickup
* bye
    - utter_goodbye

## interactive_story_1
* show{"object_color": "pink"}
    - slot{"object_color": "pink"}
    - utter_unknown_color
* affirmative
    - utter_prompt
* find{"object_color": "pink", "object_name": "apple"}
    - slot{"object_color": "pink"}
    - slot{"object_name": "apple"}
    - utter_unknown_color
* find{"object_color": "red", "object_name": "apple"}
    - slot{"object_color": "red"}
    - slot{"object_name": "apple"}
    - execute_find
* pick up
    - slot{"object_color": "red"}
    - slot{"object_name": "apple"}
    - utter_repeat_command
* affirmative
    - execute_pickup
* bye
    - utter_goodbye
