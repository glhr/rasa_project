npx chatito find.chatito --format=rasa --autoAliases=warn --trainingFileName=find.json
python3 convert_training_data.py
rm rasa_dataset_testing.json
