
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
    - slot{"object_name": "ball"}
    - got_action
    - slot{"action": "pick up"}
    - utter_unknown_object
* clarify{"object_color": "blue"}
    - slot{"object_color": "blue"}
    - utter_unknown_object
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
* clarify{"object_name": "banana"}
    - slot{"object_name": "banana"}
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
* find{"object_name": "banana"}
    - slot{"object_name": "banana"}
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
* find{"object_name": "banana"}
    - slot{"object_name": "banana"}
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

## interactive_story_1
* none
    - utter_prompt
* find{"placement": "left"}
    - slot{"placement": "left"}
    - got_action
    - slot{"action": "find"}
    - utter_prompt_object
* clarify{"object_color": "green", "object_name": "apple"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - got_action
    - execute_find
* none
    - utter_prompt

## interactive_story_1
* show
    - got_action
    - slot{"action": "learn"}
    - utter_prompt_object
* show{"placement": "middle", "object_color": "green", "object_name": "apple"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - slot{"placement": "middle"}
    - got_action
    - slot{"action": "learn"}
    - utter_got_description
    - execute_learn
    - reset_slots
* show
    - got_action
    - slot{"action": "learn"}
    - utter_prompt_object
* show{"object_name": "apple"}
    - slot{"object_name": "apple"}
    - got_action
    - slot{"action": "learn"}
    - utter_prompt_color
* clarify{"object_color": "green"}
    - slot{"object_color": "green"}
    - utter_got_description
    - execute_learn
    - reset_slots

## interactive_story_1
* show{"object_name": "duck"}
    - slot{"object_name": "duck"}
    - got_action
    - slot{"action": "learn"}
    - utter_prompt_color
* clarify{"object_color": "yellow"}
    - slot{"object_color": "yellow"}
    - utter_got_description
    - execute_learn
    - reset_slots
* pick up
    - got_action
    - slot{"action": "pick up"}
    - utter_prompt_object
* clarify{"object_color": "yellow", "object_name": "duck"}
    - slot{"object_color": "yellow"}
    - slot{"object_name": "duck"}
    - utter_unknown_object
* deny
    - cancel_command
    - reset_slots
    - utter_got_denied
* pick up{"object_color": "green", "object_name": "apple"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - got_action
    - slot{"action": "pick up"}
    - utter_repeat_command
* affirmative
    - execute_pickup

## interactive_story_1
* show{"object_color": "red", "object_name": "ball"}
    - slot{"object_color": "red"}
    - slot{"object_name": "ball"}
    - got_action
    - slot{"action": "learn"}
    - utter_got_description
    - execute_learn
    - reset_slots
* none
    - utter_prompt
* pick up{"object_name": "orange", "placement": "right"}
    - slot{"object_name": "orange"}
    - slot{"placement": "right"}
    - got_action
    - slot{"action": "pick up"}
    - utter_prompt_color
* clarify{"object_color": "orange"}
    - slot{"object_color": "orange"}
    - utter_repeat_command
* affirmative
    - execute_pickup
* greetings
    - utter_greet
    - utter_prompt
* pick up{"object_name": "object"}
    - slot{"object_name": "object"}
    - got_action
    - slot{"action": "pick up"}
    - utter_prompt_object
* pick up{"object_color": "orange", "object_name": "banana", "placement": "middle"}
    - slot{"object_color": "orange"}
    - slot{"object_name": "banana"}
    - slot{"placement": "middle"}
    - got_action
    - slot{"action": "pick up"}
    - utter_repeat_command
* affirmative
    - execute_pickup

## interactive_story_1
* move{"object_name": "apple", "placement": "right"}
    - slot{"object_name": "apple"}
    - slot{"placement": "right"}
    - got_action
    - slot{"action": "move"}
    - utter_prompt_color
* clarify{"object_name": "apple", "object_color": "green"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - utter_repeat_command
* affirmative
    - execute_move
* none
    - utter_prompt
* pick up
    - got_action
    - slot{"action": "pick up"}
    - utter_repeat_command
* move{"object_name": "orange", "placement": "middle"}
    - slot{"object_name": "orange"}
    - slot{"placement": "middle"}
    - got_action
    - slot{"action": "move"}
    - utter_repeat_command
* affirmative
    - execute_move

## interactive_story_1
* pick up{"placement": "left"}
    - slot{"placement": "left"}
    - got_action
    - slot{"action": "pick up"}
    - utter_prompt_object
* clarify{"object_color": "green", "object_name": "ball"}
    - slot{"object_color": "green"}
    - slot{"object_name": "ball"}
    - got_action
    - utter_unknown_object
* show{"object_color": "green", "object_name": "ball"}
    - slot{"object_color": "green"}
    - slot{"object_name": "ball"}
    - got_action
    - slot{"action": "learn"}
    - utter_got_description
    - execute_learn
    - reset_slots
* bye
    - utter_goodbye

## interactive_story_1
* pick up{"object_name": "balls"}
    - slot{"object_name": "balls"}
    - got_action
    - slot{"action": "pick up"}
    - utter_unknown_object
* show{"object_name": "ball", "placement": "table"}
    - slot{"object_name": "ball"}
    - slot{"placement": "table"}
    - got_action
    - slot{"action": "learn"}
    - utter_prompt_color
* clarify{"object_color": "blue"}
    - slot{"object_color": "blue"}
    - utter_prompt_placement
* clarify{"placement": "left"}
    - slot{"placement": "left"}
    - utter_got_description
    - execute_learn
    - reset_slots

## interactive_story_1
* greetings
    - utter_greet
    - utter_prompt
* find{"object_color": "green", "object_name": "apple"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - got_action
    - slot{"action": "find"}
    - execute_find
* pick up
    - got_action
    - slot{"action": "pick up"}
    - utter_repeat_command
* move{"placement": "right"}
    - slot{"placement": "right"}
    - got_action
    - slot{"action": "move"}
    - utter_repeat_command
* affirmative
    - execute_move

## interactive_story_1
* greetings
    - utter_greet
    - utter_prompt
* pick up{"object_name": "something"}
    - slot{"object_name": "something"}
    - got_action
    - slot{"action": "pick up"}
    - utter_prompt_object
* clarify{"object_color": "green", "object_name": "apple", "placement": "right"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - slot{"placement": "right"}
    - got_action
    - utter_repeat_command
* affirmative
    - execute_pickup
* bye
    - utter_goodbye
