
## interactive_story_1
* greetings
    - utter_greet
    - utter_prompt
* show{"object_name": "banana"}
    - got_action
    - utter_prompt_color
* clarify
    - utter_got_description
    - execute_learn

## interactive_story_1
* show{"object_color": "red"}
    - got_action
    - utter_prompt_object
* clarify
    - utter_got_description
    - execute_learn

## interactive_story_1
* show{"object_name": "apple"}
    - got_action
    - slot{"object_name": "apple"}
    - utter_prompt_color
* clarify{"object_color": "green"}
    - slot{"object_color": "green"}
    - utter_got_description
    - execute_learn
* none
    - utter_prompt
* pick up{"object_name": "ball"}
    - got_action
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
    - got_action
    - slot{"object_color": "pink"}
    - utter_prompt_object
* affirmative
    - utter_prompt
* find{"object_color": "pink", "object_name": "apple"}
    - got_action
    - slot{"object_color": "pink"}
    - slot{"object_name": "apple"}
    - utter_unknown_color
* find{"object_color": "red", "object_name": "apple"}
    - got_action
    - slot{"object_color": "red"}
    - slot{"object_name": "apple"}
    - execute_find
* pick up
    - got_action
    - slot{"object_color": "red"}
    - slot{"object_name": "apple"}
    - utter_repeat_command
* affirmative
    - execute_pickup
* bye
    - utter_goodbye

## interactive_story_1
* greetings
    - utter_greet
    - utter_prompt
* find
    - got_action
    - utter_prompt_object
* clarify{"object_name": "ball"}
    - slot{"object_name": "ball"}
    - utter_prompt_color
* clarify{"object_color": "blue"}
    - slot{"object_color": "blue"}
    - execute_find
* none
    - utter_prompt
* find{"object_color": "green", "object_name": "apple"}
    - got_action
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - execute_find
* bye
    - utter_goodbye

## interactive_story_1
* greetings
    - utter_greet
    - utter_prompt
* find{"object_name": "ball"}
    - slot{"object_name": "ball"}
    - got_action
    - slot{"action": "find"}
    - utter_prompt_color
* clarify{"object_color": "blue"}
    - slot{"object_color": "blue"}
    - execute_find
* none
    - utter_prompt
* bye
    - utter_goodbye
* find{"object_color": "brown", "object_name": "apple"}
    - slot{"object_color": "brown"}
    - slot{"object_name": "apple"}
    - got_action
    - slot{"action": "find"}
    - execute_find
* find{"object_color": "white"}
    - slot{"object_color": "white"}
    - got_action
    - slot{"action": "find"}
    - utter_unknown_color
* show{"object_color": "white", "object_name": "ball"}
    - slot{"object_color": "white"}
    - slot{"object_name": "ball"}
    - got_action
    - slot{"action": "learn"}
    - utter_got_description
    - execute_learn
    - reset_slots

## interactive_story_1
* greetings
    - utter_greet
    - utter_prompt
* find
    - got_action
    - slot{"action": "find"}
    - utter_prompt_object
* clarify{"object_name": "lemon"}
    - slot{"object_name": "lemon"}
    - utter_prompt_color
* clarify{"object_color": "yellow", "placement": "left"}
    - slot{"object_color": "yellow"}
    - slot{"placement": "left"}
    - execute_find

## interactive_story_1
* greetings
    - utter_greet
    - utter_prompt
* show{"object_name": "object"}
    - slot{"object_name": "object"}
    - got_action
    - slot{"action": "learn"}
    - utter_prompt_object

## interactive_story_2
* greetings
    - utter_greet
    - utter_prompt
* find{"object_name": "ball"}
    - slot{"object_name": "ball"}
    - got_action
    - slot{"action": "find"}
    - utter_prompt_color
* clarify{"object_color": "green"}
    - slot{"object_color": "green"}
    - execute_find

## interactive_story_3
* greetings
    - utter_greet
    - utter_prompt
* find
    - got_action
    - slot{"action": "find"}
    - utter_prompt_object
* find{"object_name": "orange"}
    - slot{"object_name": "orange"}
    - utter_prompt_color
* clarify{"object_color": "orange"}
    - slot{"object_color": "orange"}
    - execute_find

## interactive_story_1
* find{"object_color": "orange", "object_name": "orange", "placement": "table"}
    - slot{"object_color": "orange"}
    - slot{"object_name": "orange"}
    - slot{"placement": "table"}
    - got_action
    - slot{"action": "find"}
    - utter_prompt_placement
* clarify{"placement": "middle"}
    - slot{"placement": "middle"}
    - execute_find
* clarify{"object_color": "orange"}
    - slot{"object_color": "orange"}
    - got_action
    - execute_find
* bye
    - utter_goodbye
