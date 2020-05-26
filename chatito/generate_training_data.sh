npx chatito commands.chatito --format=rasa --autoAliases=warn --trainingFileName=commands.json
npx chatito clarification.chatito --format=rasa --autoAliases=warn --trainingFileName=clarification.json
python3 convert_training_data.py
rm *.json
