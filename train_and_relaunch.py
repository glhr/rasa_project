import os
import sys
import platform
import subprocess

from rasa.train import train
from utils.timing import CodeTimer

pid_id_file = './pid/id'
domain_file = './domain.yml'
config_file = './config.yml'
nlu_data    = './data/'
output_path = './models/'
model_name  = 'fruits_model'

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


def train_rasa():
    with CodeTimer() as timer:
        train(
            domain=domain_file,
            config=config_file,
            training_files=nlu_data, 
            output=output_path,
            #force_training=True,
            fixed_model_name=model_name)
    time = timer.took * 0.001
    print('Training time took: {} sec.'.format(time))
    
def relaunch_rasa():
    os.system("python rasa_main.py run --enable-api -p 5005")

if __name__ == "__main__":
    kill_rasa()
    train_rasa()
    relaunch_rasa()