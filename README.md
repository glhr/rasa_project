
# RASA project
Task-oriented dialogue system for talking to a robotic manipulator. Built using the RASA chat-bot framework. 
This was developed for the Little Helper 7+ at Aalborg University, however it can also be run as a stand-alone application. 
## Requirements
```
pip3 install -r requirements.txt --user
```

## Use Guide

The following commands should be run from the ``rasa_project`` folder. *Note: if you get a ``command not found`` error when running the ``rasa`` commands below even though ``rasa`` is installed, use ``python3 -m rasa`` instead.*
### Model
A model is already present in the repository (file ``models/model.tar.gaz``).  It was trained using the pipe-line specified in ``config.yml`` using all the training data in the ``data`` folder.

To re-train the model:
```
rasa train --domain=./domain.yml --config=./config.yml --fixed-model-name=model
```
### Running the chat-bot
#### Launch the action server
Run the actions server (handlers defined in ``rasa_project/actions.py``):
```
rasa run actions
```
This will run an action server at [http://localhost:5055](http://localhost:5055)
Note: make sure the action endpoint is specified in ```endpoints.yml```.

#### Talk from the command line
To talk to the chatbot in the command line:
```
rasa shell
```
To run the chatbot in interactive mode (where the user gives feedback about whether the intent, entities and response are correct):
```
rasa interactive -m .\models\model.tar.gz
```
#### Talk from the web-app
In three separate terminals:

***Launch the web-app***
```console
cd rasa-webapp && python3 main.py
```
***Start a RASA assistant***
```
rasa run --enable-api -p 5005
```
This will start a RASA assistant on http://localhost:5005

***Start an HTTP server for sending the image files to the client***
```
python -m http.server 8888
```

Now open [http://localhost:8080/](http://localhost:8080/) in a browser to see the voice interface.
