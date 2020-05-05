import logging
import platform
import subprocess
import sys

from rasa.train import train

logger = logging.getLogger(__name__)

domain_file = './domain.yml'
config_file = './config.yml'
nlu_data = './data/nlu/'
output_path = './models/'
model_name = 'fruits_model'

def train_rasa():
    train(
        domain=domain_file,
        config=config_file,
        training_files=nlu_data, 
        output=output_path,
        #force_training=True,
        fixed_model_name=model_name)

    try:
        test = platform.uname()
        if test[0] == "Linux":
            subprocess.call(['./nlp_magic/bin/rasa_actions.sh'])
            subprocess.call(['./nlp_magic/bin/rasa_bot.sh'])
        else:
            return []
    except Exception as e:
        logger.warning("Failed because not a Linux OS: {}".format(e))
    
#if __name__ == "__main__":
#    train_rasa()