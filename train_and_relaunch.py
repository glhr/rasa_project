import logging
import platform
import subprocess
import sys

from rasa.train import train
from utils.timing import CodeTimer

logger = logging.getLogger(__name__)

domain_file = './domain.yml'
config_file = './config.yml'
nlu_data = './data/'
output_path = './models/'
model_name = 'fruits_model'


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

    try:
        test = platform.uname()
        if test[0] == "Linux":
            subprocess.call(['./nlp_magic/bin/rasa_bot.sh'])
        else:
            return []
    except Exception as e:
        logger.warning("Failed because not a Linux OS: {}".format(e))
    
#if __name__ == "__main__":
#    train_rasa()