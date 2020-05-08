npx chatito find.chatito --format=rasa --autoAliases=warn --trainingFileName=find.json
npx chatito clarification.chatito --format=rasa --autoAliases=warn --trainingFileName=clarification.json
python3 convert_training_data.py
rm *.json
