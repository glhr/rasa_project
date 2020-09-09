## action
* find
    - action_fill

## action
* show
    - action_fill

## action
* pick up
    - action_fill

## action
* move
    - action_fill

<!-- out of scope talk -->
## story
* none
   - utter_prompt

## story_name
* none
  - utter_prompt
* none
  - action_fallback

<!-- cancel command -->

## deny
* deny
  - action_cancel
  - utter_got_denied

## deny
* deny{"object_name": "banana"}
  - slot{"object_name": "banana"}
  - utter_command_repeat

## deny
* deny{"object_color": "blue"}
  - slot{"object_color": "blue"}
  - utter_command_repeat

<!-- learning unknown color -->
## unknown_color
* show{"object_color": "pink"}
  - slot{"object_color": "pink"}
  - action_fill
  - slot{"action": "learn"}
  - utter_prompt_object

<!-- got unknown color -->
## unknown_color
* find{"object_color": "white"}
  - slot{"object_color": "white"}
  - action_fill
  - slot{"action": "find"}
  - utter_got_unknown_color

## unknown_color
* pick up{"object_color": "white"}
  - slot{"object_color": "white"}
  - action_fill
  - slot{"action": "pick up"}
  - utter_got_unknown_color

<!-- find -->

<!-- missing color in find command -->
## find
* find{"object_name": "apple"}
  - slot{"object_name": "apple"}
  - action_fill
  - slot{"action": "find"}
  - utter_prompt_color

<!-- unknown object in find command -->
## find
* find{"object_name": "duck"}
  - slot{"object_name": "duck"}
  - action_fill
  - slot{"action": "find"}
  - utter_got_unknown_object

<!-- missing color in find command -->
## find
* find{"object_color": "green"}
  - slot{"object_color": "green"}
  - action_fill
  - slot{"action": "find"}
  - utter_prompt_object

<!-- valid find command -->
## find
* find{"object_name": "apple", "object_color": "green"}
  - slot{"object_name": "apple"}
  - slot{"object_color": "green"}
  - action_fill
  - slot{"action": "find"}
  - utter_got_command
  - execute_find

<!-- known object but unknown color in find command -->
## find
* find{"object_name": "apple", "object_color": "white"}
  - slot{"object_name": "apple"}
  - slot{"object_color": "white"}
  - action_fill
  - slot{"action": "find"}
  - utter_got_unknown_color

<!-- SHOW: object name or color is missing -->
## show
* show{"object_name": "apple"}
  - slot{"object_name": "apple"}
  - action_fill
  - slot{"action": "learn"}
  - utter_prompt_color

## show
* show{"object_color": "red"}
  - slot{"object_color": "red"}
  - action_fill
  - slot{"action": "learn"}
  - utter_prompt_object
* clarify{"object_name": "banana", "object_color": "yellow"}
  - slot{"object_name": "banana"}
  - slot{"object_color": "yellow"}
  - utter_got_command
  - execute_learn

## show
* show{"object_color": "green"}
  - slot{"object_color": "green"}
  - action_fill
  - slot{"action": "learn"}
  - utter_prompt_object
* clarify{"object_name": "banana", "object_color": "blue"}
  - slot{"object_name": "banana"}
  - slot{"object_color": "blue"}
  - utter_got_command
  - execute_learn

## show
* show{"object_color": "pink"}
  - slot{"object_color": "pink"}
  - action_fill
  - slot{"action": "learn"}
  - utter_prompt_object
* clarify{"object_color": "blue"}
  - slot{"object_color": "blue"}
  - utter_prompt_object
* clarify{"object_name": "banana"}
  - slot{"object_name": "banana"}
  - utter_got_command
  - execute_learn

## show
* show{"object_name": "banana"}
  - slot{"object_name": "banana"}
  - action_fill
  - slot{"action": "learn"}
  - utter_prompt_color
* clarify{"object_name": "apple", "object_color": "purple"}
  - slot{"object_name": "apple"}
  - slot{"object_color": "purple"}
  - utter_got_command
  - execute_learn

## show
* show{"object_color": "black", "object_name": "banana"}
  - slot{"object_color": "black"}
  - slot{"object_name": "banana"}
  - action_fill
  - slot{"action": "learn"}
  - utter_got_command
  - execute_learn

<!-- confirm pickup -->

## story_name
* none
  - utter_prompt
* pick up{"object_name": "apple"}
  - slot{"object_name": "apple"}
  - action_fill
  - slot{"action": "pick up"}
  - utter_prompt_color
* affirmative
  - utter_prompt_color
* clarify{"object_name": "orange", "object_color": "orange"}
  - slot{"object_name": "orange"}
  - slot{"object_color": "orange"}
  - utter_command_repeat
* affirmative
  - utter_got_command
  - execute_pickup

## story_name
* pick up{"object_color": "brown", "object_name": "strawberry"}
  - slot{"object_color": "brown"}
  - slot{"object_name": "strawberry"}
  - action_fill
  - slot{"action": "pick up"}
  - utter_command_repeat
* affirmative
  - utter_got_command
  - execute_pickup

## story_name
* pick up{"object_color": "black", "object_name": "kiwi"}
  - slot{"object_color": "black"}
  - slot{"object_name": "kiwi"}
  - action_fill
  - slot{"action": "pick up"}
  - utter_command_repeat
* affirmative
  - utter_got_command
  - execute_pickup
