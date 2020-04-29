# rasa_project
RASA NLP project for talking to a robotic manipulator

## Use Guide

You can use the script **```parse-wit-expressions.py```** to generate a RASA-compatible JSON file for training (input: wit_data/expressions.json, output: rasa_project/data/nlu.json)

The following commands should be run from the ``rasa_project`` folder.

To train the core + NLU model:
**```rasa train```** (model is saved as tar.gz file in rasa_project/models) or ```rasa train nlu``` to train NLU only.

To run the actions server (handlers defined in rasa_project/actions.py):
**```rasa run actions```**. This will run an action server at [http://localhost:5055](http://localhost:5055)
Note: make sure the action endpoint is specified in ```endpoints.yml```.

To test the chatbot in the command line:
**```rasa shell```**

To run the chatbot in interactive mode (where the user gives feedback about whether the intent, entities and response are correct):
**```rasa interactive -m .\models\20200217-154233.tar.gz```**

### For running the front-end (connected via sockets)
**```cd rasa_project```**

***Build the web-app:***

For `rasa-webapp`:

```console
cd rasa-webapp/static
npm install #only run this the first time
npm run build
cd ../
python3 main.py
```

For `rasa-voice-interface`:

```console
cd rasa-voice-interface
npm install #only run this the first time
npm run serve
```

This will launch the voice interface at https://localhost:8080

***Start a RASA assistant***
``rasa run --enable-api -p 5005``
This will start a RASA assistant on http://localhost:5005

***Start the action server***
``rasa run actions``

***Start an HTTP server for sending the image files to the client***
``python -m http.server 8888``

Now open [http://localhost:8080/](http://localhost:8080/) in a browser to see the voice interface.
