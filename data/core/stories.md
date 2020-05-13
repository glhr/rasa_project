## story_name    <!-- name of the story - just for debugging -->
* greetings
   - utter_greeting
   - utter_prompt
* pick up{"object_color": "purple", "object_name": "cherry"}  <!-- user utterance, in format intent{entities} -->
   - received_command
   - utter_repeat_command
* affirmative
   - execute_command        <!-- action that the bot should execute -->
* bye
   - utter_bye

## story
* none
   - utter_prompt

## story
* greetings
  - utter_greeting
  - utter_prompt

## story
* bye
  - utter_bye

## deny
* deny
  - cancel_command
  - utter_user_denied

## show
* show{"object_color": "pink", "object_name": "orange"}
  - utter_got_description
  - execute_command

## story_name
* greetings
  - utter_greeting
  - utter_prompt
* none
  - utter_prompt
* pick up{"object_name": "apple"}
  - received_command
  - utter_prompt_color
* affirmative
  - execute_command
* bye
  - utter_bye
