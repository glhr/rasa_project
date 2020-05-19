
## interactive_story_1
* greetings
    - utter_greet_hello
    - utter_prompt
* show{"object_name": "banana"}
    - action_fill
    - slot{"action": "learn"}
    - utter_prompt_color
* clarify
    - utter_got_command
    - execute_learn

## interactive_story_1
* show{"object_color": "red"}
    - action_fill
    - slot{"action": "learn"}
    - utter_prompt_object
* clarify
    - utter_got_command
    - execute_learn

## interactive_story_1
* show{"object_name": "apple"}
    - slot{"object_name": "apple"}
    - action_fill
    - slot{"action": "learn"}
    - utter_prompt_color
* clarify{"object_color": "green"}
    - slot{"object_color": "green"}
    - utter_got_command
    - execute_learn
* none
    - utter_prompt
* pick up{"object_name": "ball"}
    - slot{"object_name": "ball"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_got_unknown_object
* clarify{"object_color": "blue"}
    - slot{"object_color": "blue"}
    - utter_got_unknown_object
* affirmative
    - utter_got_command
    - execute_pickup
* bye
    - utter_greet_goodbye

## interactive_story_1
* show{"object_color": "pink"}
    - slot{"object_color": "pink"}
    - action_fill
    - slot{"action": "learn"}
    - utter_prompt_object
* affirmative
    - utter_prompt
* find{"object_color": "pink", "object_name": "apple"}
    - slot{"object_color": "pink"}
    - slot{"object_name": "apple"}
    - action_fill
    - utter_got_unknown_color
* find{"object_color": "red", "object_name": "apple"}
    - slot{"object_color": "red"}
    - slot{"object_name": "apple"}
    - action_fill
    - slot{"action": "find"}
    - utter_got_command
    - execute_find
* pick up
    - action_fill
    - slot{"action": "pick up"}
    - utter_command_repeat
* affirmative
    - utter_got_command
    - execute_pickup
* bye
    - utter_greet_goodbye

## interactive_story_1
* greetings
    - utter_greet_hello
    - utter_prompt
* find
    - action_fill
    - utter_prompt_object
* clarify{"object_name": "banana"}
    - slot{"object_name": "banana"}
    - utter_prompt_color
* clarify{"object_color": "blue"}
    - slot{"object_color": "blue"}
    - utter_got_command
    - execute_find
* none
    - utter_prompt
* find{"object_color": "green", "object_name": "apple"}
    - action_fill
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - utter_got_command
    - execute_find
* bye
    - utter_greet_goodbye

## interactive_story_1
* greetings
    - utter_greet_hello
    - utter_prompt
* find{"object_name": "banana"}
    - slot{"object_name": "banana"}
    - action_fill
    - slot{"action": "find"}
    - utter_prompt_color
* clarify{"object_color": "blue"}
    - slot{"object_color": "blue"}
    - utter_got_command
    - execute_find
* none
    - utter_prompt
* bye
    - utter_greet_goodbye
* find{"object_color": "brown", "object_name": "apple"}
    - slot{"object_color": "brown"}
    - slot{"object_name": "apple"}
    - action_fill
    - slot{"action": "find"}
    - utter_got_command
    - execute_find
* find{"object_color": "white"}
    - slot{"object_color": "white"}
    - action_fill
    - slot{"action": "find"}
    - utter_got_unknown_color
* show{"object_color": "white", "object_name": "ball"}
    - slot{"object_color": "white"}
    - slot{"object_name": "ball"}
    - action_fill
    - slot{"action": "learn"}
    - utter_got_command
    - execute_learn
    - reset_slots

## interactive_story_1
* greetings
    - utter_greet_hello
    - utter_prompt
* find
    - action_fill
    - slot{"action": "find"}
    - utter_prompt_object
* clarify{"object_name": "lemon"}
    - slot{"object_name": "lemon"}
    - utter_prompt_color
* clarify{"object_color": "yellow", "placement": "left"}
    - slot{"object_color": "yellow"}
    - slot{"placement": "left"}
    - utter_got_command
    - execute_find

## interactive_story_1
* greetings
    - utter_greet_hello
    - utter_prompt
* show{"object_name": "object"}
    - slot{"object_name": "object"}
    - action_fill
    - slot{"action": "learn"}
    - utter_prompt_object

## interactive_story_2
* greetings
    - utter_greet_hello
    - utter_prompt
* find{"object_name": "banana"}
    - slot{"object_name": "banana"}
    - action_fill
    - slot{"action": "find"}
    - utter_prompt_color
* clarify{"object_color": "green"}
    - slot{"object_color": "green"}
    - utter_got_command
    - execute_find

## interactive_story_3
* greetings
    - utter_greet_hello
    - utter_prompt
* find
    - action_fill
    - slot{"action": "find"}
    - utter_prompt_object
* find{"object_name": "orange"}
    - slot{"object_name": "orange"}
    - utter_prompt_color
* clarify{"object_color": "orange"}
    - slot{"object_color": "orange"}
    - utter_got_command
    - execute_find

## interactive_story_1
* find{"object_color": "orange", "object_name": "orange", "placement": "table"}
    - slot{"object_color": "orange"}
    - slot{"object_name": "orange"}
    - slot{"placement": "table"}
    - action_fill
    - slot{"action": "find"}
    - utter_prompt_placement_origin
* clarify{"placement": "middle"}
    - slot{"placement": "middle"}
    - utter_got_command
    - execute_find
* clarify{"object_color": "orange"}
    - slot{"object_color": "orange"}
    - action_fill
    - utter_got_command
    - execute_find
* bye
    - utter_greet_goodbye

## interactive_story_1
* none
    - utter_prompt
* find{"placement": "left"}
    - slot{"placement": "left"}
    - action_fill
    - slot{"action": "find"}
    - utter_prompt_object
* clarify{"object_color": "green", "object_name": "apple"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - action_fill
    - utter_got_command
    - execute_find
* none
    - utter_prompt

## interactive_story_1
* show
    - action_fill
    - slot{"action": "learn"}
    - utter_prompt_object
* show{"placement": "middle", "object_color": "green", "object_name": "apple"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - slot{"placement": "middle"}
    - action_fill
    - slot{"action": "learn"}
    - utter_got_command
    - execute_learn
    - reset_slots
* show
    - action_fill
    - slot{"action": "learn"}
    - utter_prompt_object
* show{"object_name": "apple"}
    - slot{"object_name": "apple"}
    - action_fill
    - slot{"action": "learn"}
    - utter_prompt_color
* clarify{"object_color": "green"}
    - slot{"object_color": "green"}
    - utter_got_command
    - execute_learn
    - reset_slots

## interactive_story_1
* show{"object_name": "duck"}
    - slot{"object_name": "duck"}
    - action_fill
    - slot{"action": "learn"}
    - utter_prompt_color
* clarify{"object_color": "yellow"}
    - slot{"object_color": "yellow"}
    - utter_got_command
    - execute_learn
    - reset_slots
* pick up
    - action_fill
    - slot{"action": "pick up"}
    - utter_prompt_object
* clarify{"object_color": "yellow", "object_name": "duck"}
    - slot{"object_color": "yellow"}
    - slot{"object_name": "duck"}
    - utter_got_unknown_object
* deny
    - action_cancel
    - reset_slots
    - utter_got_denied
* pick up{"object_color": "green", "object_name": "apple"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_command_repeat
* affirmative
    - utter_got_command
    - execute_pickup

## interactive_story_1
* show{"object_color": "red", "object_name": "ball"}
    - slot{"object_color": "red"}
    - slot{"object_name": "ball"}
    - action_fill
    - slot{"action": "learn"}
    - execute_learn
    - reset_slots
* none
    - utter_prompt
* pick up{"object_name": "orange", "placement": "right"}
    - slot{"object_name": "orange"}
    - slot{"placement": "right"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_prompt_color
* clarify{"object_color": "orange"}
    - slot{"object_color": "orange"}
    - utter_command_repeat_withplacement_origin
* affirmative
    - utter_got_command
    - execute_pickup
* greetings
    - utter_greet_hello
    - utter_prompt
* pick up{"object_name": "object"}
    - slot{"object_name": "object"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_prompt_object
* pick up{"object_color": "orange", "object_name": "banana", "placement": "middle"}
    - slot{"object_color": "orange"}
    - slot{"object_name": "banana"}
    - slot{"placement": "middle"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_command_repeat_withplacement_origin
* affirmative
    - utter_got_command
    - execute_pickup

## interactive_story_1
* move{"object_name": "apple", "placement": "right"}
    - slot{"object_name": "apple"}
    - slot{"placement": "right"}
    - action_fill
    - slot{"action": "move"}
    - utter_prompt_color
* clarify{"object_name": "apple", "object_color": "green"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - utter_command_repeat_withplacement_destination
* affirmative
    - utter_got_command
    - execute_move
* none
    - utter_prompt
* pick up
    - action_fill
    - slot{"action": "pick up"}
    - utter_command_repeat
* move{"object_name": "orange", "placement": "middle"}
    - slot{"object_name": "orange"}
    - slot{"placement": "middle"}
    - action_fill
    - slot{"action": "move"}
    - utter_command_repeat_withplacement_destination
* affirmative
    - utter_got_command
    - execute_move

## interactive_story_1
* pick up{"placement": "left"}
    - slot{"placement": "left"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_prompt_object
* clarify{"object_color": "green", "object_name": "ball"}
    - slot{"object_color": "green"}
    - slot{"object_name": "ball"}
    - action_fill
    - utter_got_unknown_object
* show{"object_color": "green", "object_name": "ball"}
    - slot{"object_color": "green"}
    - slot{"object_name": "ball"}
    - action_fill
    - slot{"action": "learn"}
    - utter_got_command
    - execute_learn
    - reset_slots
* bye
    - utter_greet_goodbye

## interactive_story_1
* pick up{"object_name": "balls"}
    - slot{"object_name": "balls"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_got_unknown_object
* show{"object_name": "ball", "placement": "table"}
    - slot{"object_name": "ball"}
    - slot{"placement": "table"}
    - action_fill
    - slot{"action": "learn"}
    - utter_prompt_color
* clarify{"object_color": "blue"}
    - slot{"object_color": "blue"}
    - utter_prompt_placement_origin
* clarify{"placement": "left"}
    - slot{"placement": "left"}
    - execute_learn
    - reset_slots

## interactive_story_1
* greetings
    - utter_greet_hello
    - utter_prompt
* find{"object_color": "green", "object_name": "apple"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - action_fill
    - slot{"action": "find"}
    - utter_got_command
    - execute_find
* pick up
    - action_fill
    - slot{"action": "pick up"}
    - utter_command_repeat
* move{"placement": "right"}
    - slot{"placement": "right"}
    - action_fill
    - slot{"action": "move"}
    - utter_command_repeat_withplacement_destination
* affirmative
    - utter_got_command
    - execute_move

## interactive_story_1
* greetings
    - utter_greet_hello
    - utter_prompt
* pick up{"object_name": "something"}
    - slot{"object_name": "something"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_prompt_object
* clarify{"object_color": "green", "object_name": "apple", "placement": "right"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - slot{"placement": "right"}
    - action_fill
    - utter_command_repeat_withplacement_origin
* affirmative
    - utter_got_command
    - execute_pickup
* bye
    - utter_greet_goodbye

## interactive_story_1
* show{"object_color": "green", "object_name": "apple", "placement": "middle"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - slot{"placement": "middle"}
    - action_fill
    - slot{"action": "learn"}
    - utter_got_command
    - execute_learn
    - reset_slots
* none
    - utter_prompt
* find{"object_color": "yellow", "object_name": "banana", "placement": "right"}
    - slot{"object_color": "yellow"}
    - slot{"object_name": "banana"}
    - slot{"placement": "right"}
    - action_fill
    - slot{"action": "find"}
    - utter_got_command
    - execute_find
* pick up
    - action_fill
    - slot{"action": "pick up"}
    - utter_command_repeat
* affirmative
    - utter_got_command
    - execute_pickup
* pick up{"object_color": "green", "object_name": "apple"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_command_repeat
* pick up{"object_name": "banana"}
    - slot{"object_name": "banana"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_command_repeat
* clarify{"object_color": "yellow"}
    - slot{"object_color": "yellow"}
    - action_fill
    - utter_command_repeat_withplacement_origin
* affirmative
    - utter_got_command
    - execute_pickup

## interactive_story_1
* move{"object_name": "apple", "placement": "right"}
    - slot{"object_name": "apple"}
    - slot{"placement": "right"}
    - action_fill
    - slot{"action": "move"}
    - utter_prompt_color
* clarify{"object_name": "apple", "object_color": "green"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - utter_command_repeat_withplacement_destination
* move{"placement": "left"}
    - slot{"placement": "left"}
    - action_fill
    - slot{"action": "move"}
    - utter_command_repeat_withplacement_destination
* affirmative
    - utter_got_command
    - execute_move
* bye
    - utter_greet_goodbye

## interactive_story_1
* show{"object_name": "object"}
    - slot{"object_name": "object"}
    - action_fill
    - slot{"action": "learn"}
    - utter_prompt_object
* show{"object_name": "strawberry"}
    - slot{"object_name": "strawberry"}
    - action_fill
    - slot{"action": "learn"}
    - utter_prompt_color
* clarify{"object_color": "red"}
    - slot{"object_color": "red"}
    - utter_got_command
    - execute_learn
    - reset_slots
* find
    - action_fill
    - slot{"action": "find"}
    - utter_prompt_object
* clarify{"object_name": "banana"}
    - slot{"object_name": "banana"}
    - utter_prompt_color
* clarify{"object_color": "brown"}
    - slot{"object_color": "brown"}
    - utter_got_command
    - execute_find

## interactive_story_1
* find{"placement": "table", "object_color": "pink"}
    - slot{"object_color": "pink"}
    - slot{"placement": "table"}
    - action_fill
    - slot{"action": "find"}
    - utter_got_unknown_color
* find{"object_color": "red"}
    - slot{"object_color": "red"}
    - action_fill
    - slot{"action": "find"}
    - utter_prompt_object
* clarify{"object_name": "cherry"}
    - slot{"object_name": "cherry"}
    - action_fill
    - utter_got_unknown_object
* show{"object_name": "cherry"}
    - slot{"object_name": "cherry"}
    - action_fill
    - slot{"action": "learn"}
    - utter_got_command
    - execute_learn
    - reset_slots
* show
    - action_fill
    - slot{"action": "learn"}
    - utter_prompt_object
* show{"object_name": "grapefruit", "object_color": "orange"}
    - slot{"object_color": "orange"}
    - slot{"object_name": "grapefruit"}
    - action_fill
    - slot{"action": "learn"}
    - utter_got_command
    - execute_learn
    - reset_slots
* none
    - utter_prompt
* none
    - utter_prompt
* none
    - utter_prompt
* bye
    - utter_greet_goodbye

## interactive_story_1
* bye
    - utter_prompt
* none
    - utter_prompt
* find{"placement": "table"}
    - slot{"placement": "table"}
    - action_fill
    - slot{"action": "find"}
    - utter_prompt_object
* deny
    - action_cancel
    - reset_slots
    - utter_got_denied
* none
    - utter_prompt
* deny
    - utter_prompt
* deny
    - utter_prompt
* none
    - utter_prompt
* pick up{"object_name": "something"}
    - slot{"object_name": "something"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_prompt_object
* clarify{"object_name": "book"}
    - slot{"object_name": "book"}
    - utter_got_unknown_object
* none{"object_name": "objects"}
    - slot{"object_name": "objects"}
    - utter_prompt
* pick up{"object_name": "fruit"}
    - slot{"object_name": "fruit"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_prompt_object
* clarify{"object_name": "raspberry"}
    - slot{"object_name": "raspberry"}
    - utter_got_unknown_object
* deny
    - action_cancel
    - reset_slots
    - utter_got_denied

## interactive_story_1
* pick up{"object_color": "green", "object_name": "thing"}
    - slot{"object_color": "green"}
    - slot{"object_name": "thing"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_prompt_object
* clarify{"object_name": "apple"}
    - slot{"object_name": "apple"}
    - action_fill
    - utter_command_repeat
* affirmative
    - utter_got_command
    - execute_pickup
    - reset_slots
* pick up{"object_name": "banana"}
    - slot{"object_name": "banana"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_prompt_color
* clarify{"object_color": "orange"}
    - slot{"object_color": "orange"}
    - utter_command_repeat
* affirmative
    - utter_got_command
    - execute_pickup
    - reset_slots

## interactive_story_1
* clarify{"object_color": "blue", "object_name": "object"}
    - slot{"object_color": "blue"}
    - slot{"object_name": "object"}
    - utter_prompt_action
* find
    - action_fill
    - slot{"action": "find"}
    - utter_prompt_object
* clarify{"object_name": "ball"}
    - slot{"object_name": "ball"}
    - utter_got_command
    - execute_find
    - reset_slots

## interactive_story_1
* pick up{"object_name": "apple", "placement": "table"}
    - slot{"object_name": "apple"}
    - slot{"placement": "table"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_prompt_color
* clarify{"object_color": "pink"}
    - slot{"object_color": "pink"}
    - utter_got_unknown_color
* clarify{"object_color": "purple"}
    - slot{"object_color": "purple"}
    - utter_prompt_placement_origin
* clarify{"placement": "left"}
    - slot{"placement": "left"}
    - utter_command_repeat
* affirmative
    - utter_got_command
    - execute_pickup

## interactive_story_1
* greetings
    - utter_greet_hello
    - utter_prompt
* none
    - utter_prompt
* pick up{"object_name": "cup"}
    - slot{"object_name": "cup"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_got_unknown_object
* pick up
    - action_fill
    - slot{"action": "pick up"}
    - utter_prompt_object
* pick up{"object_name": "ball"}
    - slot{"object_name": "ball"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_got_unknown_object
* clarify{"object_name": "apple"}
    - slot{"object_name": "apple"}
    - action_fill
    - utter_prompt_color
* clarify{"object_color": "green"}
    - slot{"object_color": "green"}
    - utter_command_repeat
* affirmative
    - utter_got_command
    - execute_pickup
    - reset_slots

## interactive_story_1
* pick up{"object_name": "something"}
    - slot{"object_name": "something"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_prompt_object
* move{"object_name": "apple", "placement": "right"}
    - slot{"object_name": "apple"}
    - slot{"placement": "right"}
    - action_fill
    - slot{"action": "move"}
    - utter_prompt_color
* clarify{"object_name": "apple", "placement": "middle"}
    - slot{"object_name": "apple"}
    - slot{"placement": "middle"}
    - utter_prompt_color
* clarify{"object_color": "gray"}
    - slot{"object_color": "gray"}
    - utter_got_unknown_color
* deny
    - action_cancel
    - reset_slots
    - utter_got_denied

## interactive_story_1
* greetings
    - utter_greet_hello
    - utter_prompt
* pick up{"object_color": "green", "object_name": "apple", "placement": "left"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - slot{"placement": "left"}
    - action_fill
    - slot{"action": "pick up"}
    - utter_command_repeat_withplacement_origin
* affirmative
    - utter_got_command
    - execute_pickup
    - reset_slots

## interactive_story_1
* greetings
    - utter_greet_hello
    - utter_prompt
* find{"object_color": "green", "object_name": "apple"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - action_fill
    - slot{"action": "find"}
    - utter_got_command
    - execute_find
    - reset_slots
* deny
    - action_cancel
    - reset_slots
    - utter_got_denied
* find{"object_color": "green", "object_name": "apple", "placement": "right"}
    - slot{"object_color": "green"}
    - slot{"object_name": "apple"}
    - slot{"placement": "right"}
    - action_fill
    - slot{"action": "find"}
    - utter_got_command
    - execute_find
    - reset_slots

## interactive_story_1
* bye
    - utter_prompt
