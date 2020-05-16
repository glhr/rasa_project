<!-- out of scope talk -->
## story
* none
   - utter_prompt

## story_name
* none
  - utter_prompt
* none
  - utter_prompt

<!-- cancel command -->

## deny
* deny
  - cancel_command
  - utter_got_denied

## deny
* deny{"object_name": "banana"}
  - slot{"object_name": "banana"}
  - utter_repeat_command

## deny
* deny{"object_color": "blue"}
  - slot{"object_color": "blue"}
  - utter_repeat_command

<!-- unknown color -->
## unknown_color
* show{"object_color": "pink"}
  - slot{"object_color": "pink"}
  - utter_unknown_color

## unknown_color
* find{"object_color": "white"}
  - slot{"object_color": "white"}
  - utter_unknown_color

## unknown_color
* pick up{"object_color": "white"}
  - slot{"object_color": "white"}
  - utter_unknown_color

<!-- find -->
## find
* find
  - execute_find

## find
* find{"object_name": "apple"}
  - slot{"object_name": "apple"}
  - utter_prompt_color

## find
* find{"object_name": "duck"}
  - slot{"object_name": "duck"}
  - utter_unknown_object

## find
* find{"object_color": "green"}
  - slot{"object_color": "green"}
  - utter_prompt_object

## find
* find{"object_name": "apple", "object_color": "green"}
  - slot{"object_name": "apple", "object_color": "green"}
  - execute_find

## find
* find{"object_name": "apple", "object_color": "white"}
  - slot{"object_name": "apple", "object_color": "white"}
  - utter_unknown_color

<!-- SHOW: object name or color is missing -->
## show
* show{"object_name": "apple"}
  - slot{"object_name": "apple"}
  - utter_prompt_color

## show
* show{"object_color": "red"}
  - slot{"object_color": "red"}
  - utter_prompt_object
* clarify{"object_name": "banana", "object_color": "yellow"}
  - slot{"object_name": "banana", "object_color": "yellow"}
  - utter_got_description
  - execute_learn

## show
* show{"object_color": "green"}
  - slot{"object_color": "green"}
  - utter_prompt_object
* clarify{"object_name": "banana", "object_color": "blue"}
  - slot{"object_name": "banana", "object_color": "blue"}
  - utter_got_description
  - execute_learn

## show
* show{"object_color": "pink"}
  - slot{"object_color": "pink"}
  - utter_unknown_color
* clarify{"object_color": "blue"}
  - slot{"object_color": "blue"}
  - utter_prompt_object
* clarify{"object_name": "banana"}
  - slot{"object_name": "banana"}
  - utter_got_description
  - execute_learn

## show
* show{"object_name": "banana"}
  - slot{"object_name": "banana"}
  - utter_prompt_color
* clarify{"object_name": "apple", "object_color": "purple"}
  - slot{"object_name": "apple", "object_color": "purple"}
  - utter_got_description
  - execute_learn

## show
* show{"object_color": "black", "object_name": "banana"}
  - slot{"object_color": "black", "object_name": "banana"}
  - utter_got_description
  - execute_learn

<!-- confirm pickup -->

## story_name
* none
  - utter_prompt
* pick up{"object_name": "apple"}
  - slot{"object_name": "apple"}
  - utter_prompt_color
* affirmative
  - utter_prompt_color
* clarify{"object_name": "orange", "object_color": "orange"}
  - slot{"object_name": "orange", "object_color": "orange"}
  - utter_repeat_command
* affirmative
  - execute_pickup

## story_name
* pick up{"object_color": "brown", "object_name": "strawberry"}
  - slot{"object_color": "brown", "object_name": "strawberry"}
  - utter_repeat_command
* affirmative
  - execute_pickup

## story_name
* pick up{"object_color": "black", "object_name": "kiwi"}
  - slot{"object_color": "black", "object_name": "kiwi"}
  - utter_repeat_command
* affirmative
  - execute_pickup
