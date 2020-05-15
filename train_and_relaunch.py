import os
import sys
import json
import pickle
import platform
import subprocess

import timeit
import time

from rasa.train import train
#from utils.timing import CodeTimer

pid_id_file = './pid/id'
domain_file = './domain.yml'
config_file = './config.yml'
nlu_data    = './data/'
output_path = './models/'
model_name  = 'fruits_model'

filename = './results/pipeline_training_duration.json'

class CodeTimer:
    def __init__(self, name=None):
        self.name = " '"  + name + "'" if name else ''

    def __enter__(self):
        self.start = timeit.default_timer()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.took = (timeit.default_timer() - self.start) * 1000.0
        # print('Code block' + self.name + ' took: ' + str(self.took) + ' ms')
        return None

def kill_rasa():
    f = open(pid_id_file, 'r')
    id = f.readlines()
    id = [str(i) for i in id]
    id = "".join(id)
    id = str(id)
    f.close()
    test = platform.uname()
    if test[0] == "Linux":
        os.system("kill " + id)
    else:
        os.system("taskkill /F /PID " + id)


def train_rasa(pipeline_name):
    if pipeline_name == config_file:
        pipeline_name = config_file
    else:
        pipeline_file = './pipelines/' + pipeline_name
    with CodeTimer() as timer:
        train(
            domain=domain_file,
            config=pipeline_file,   # one of the decided pipelines
            #config=config_file,    # standard config.yml file
            training_files=nlu_data,
            #output=output_path,
            force_training=True,
            fixed_model_name=pipeline_name)
    time = str(timer.took * 0.001)
    return time


def relaunch_rasa():
    os.system("python rasa_main.py run --enable-api -p 5005")

def evaluate_pipelines():
    data = {}
    pipeline_name = ['supervised_embeddings.yml', 'pretrained_embeddings_spacy.yml', 'recommended.yml', 'custom.yml', 'mitie.yml']
    data ['supervised_embeddings']       = train_rasa(pipeline_name[0])
    data ['pretrained_embeddings_spacy'] = train_rasa(pipeline_name[1])
    data ['recommended']                 = train_rasa(pipeline_name[2])
    data ['custom']                      = train_rasa(pipeline_name[3])
    data ['mitie']                       = train_rasa(pipeline_name[4])
    json.dump(data, open(filename, 'w', encoding='utf8'))
    #data = json.load(open(filename))

if __name__ == "__main__":
    #kill_rasa()
    #train_rasa(config_file)
    #relaunch_rasa()
    evaluate_pipelines()
    