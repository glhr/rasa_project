import requests

# get the domain
headers_domain = {'Accept': "Accept: application/json"}
domain_request = requests.get("http://localhost:5005/domain", headers=headers_domain)

print(domain_request.status_code)

# train the model

train_request = {
    "domain": "intents:\n  - greet\n  - goodbye\n  - affirm\n  - deny\n  - mood_great\n  - mood_unhappy\n\nresponses:\n  utter_greet:\n  - text: \"Hey! How are you?\"\n\n  utter_cheer_up:\n  - text: \"Here is something to cheer you up:\"\n    image: \"https://i.imgur.com/nGF1K8f.jpg\"\n\n  utter_did_that_help:\n  - text: \"Did that help you?\"\n\n  utter_happy:\n  - text: \"Great carry on!\"\n\n  utter_goodbye:\n  - text: \"Bye\"",
    "config": "language: en\npipeline: supervised_embeddings\npolicies:\n  - name: MemoizationPolicy\n  - name: KerasPolicy",
    "nlu": "## intent:greet\n- hey\n- hello\n- hi\n## intent:goodbye\n- bye\n- goodbye\n- have a nice day\n- see you\n## intent:affirm\n- yes\n- indeed\n## intent:deny\n- no\n- never\n## intent:mood_great\n- perfect\n- very good\n- great\n## intent:mood_unhappy\n- sad\n- not good\n- unhappy",
    "responses": "## ask name * chitchat/ask_name\n    - my name is Sara, Rasa's documentation bot!\n\n## ask weather * chitchat/ask_weather\n    - it's always sunny where I live",
    "stories": "## happy path\n* greet\n\n  - utter_greet\n\n* mood_great\n\n  - utter_happy\n\n## sad path 1\n* greet\n\n  - utter_greet\n\n* mood_unhappy\n\n  - utter_cheer_up\n\n  - utter_did_that_help\n\n* affirm\n\n  - utter_happy\n\n## sad path 2\n* greet\n\n  - utter_greet\n\n* mood_unhappy\n\n  - utter_cheer_up\n\n  - utter_did_that_help\n\n* deny\n\n  - utter_goodbye\n\n## say goodbye\n* goodbye\n\n  - utter_goodbye",
    "force": False,
    "save_to_default_model_directory": False
}

import json
headers_train = {
    'Content-Type': "application/json",
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br"
}
train_request = requests.post("http://localhost:5005/model/train",
                             headers=headers_train,
                             data=json.dumps(train_request))

print(train_request.status_code)

if train_request.status_code == 200:
    import shutil
    # write model to file
    with open('models/test.tar.gz','wb') as f:
        train_request.raw.decode_content = True
        f.write(train_request.content)

    # load the model
    model_request = {
      "model_file": "models/test.tar.gz"
    }

    headers_model = {
        'Accept': "*/*"
    }

    load_request = requests.put("http://localhost:5005/model",
                                 headers=headers_model,
                                 data=json.dumps(model_request))

    print(load_request.status_code)
else:
    print(train_request.text[:300])
