import requests
import json
from utils.logger import get_logger

logger = get_logger()

# get the domain file from the API
headers_domain = {'Accept': "Accept: application/json"}
domain_request = requests.get("http://localhost:5005/domain", headers=headers_domain)
print(domain_request.status_code)

# load the NLU and stories data from training files
with open('pipelines/custom.yml', 'r') as f:
    config = f.read()

nlu_files = [
    'data/user-data/user_data.md',
    'data/user-data/user_data_2.md',
    'data/manually-generated/commands.md',
    'data/manually-generated/conversation.md',
    'data/auto-generated/commands.md',
    'data/auto-generated/clarification.md',
    'data/rasa-interactive/nlu.md'
    ]

stories_files = [
    'data/rasa-interactive/stories.md',
    'data/manually-generated/stories.md'
    ]


def train_model():
    nlu_data = ''
    for file in nlu_files:
        with open(file, 'r') as f:
            nlu_data += f.read()+'\n'

    stories_data = ''
    for file in stories_files:
        with open(file, 'r') as f:
            stories_data += f.read()+'\n'

    # construct a training request
    train_request = {
        "domain": domain_request.text,
        "config": config,
        "nlu": nlu_data,
        "stories": stories_data,
        "force": False,
        "save_to_default_model_directory": False
    }

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


if __name__ == "__main__":
    train_model()
