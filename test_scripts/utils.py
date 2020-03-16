import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import logging
import rasa.utils.io as io_utils
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.components import ComponentBuilder

spacy_nlp_config = {"name": "SpacyNLP"}
blank_config = RasaNLUModelConfig({"language": "en", "pipeline": []})
spacy_nlp = ComponentBuilder().create_component(spacy_nlp_config, blank_config).nlp

def logging_setup():
    logger = logging.getLogger(__name__)
    logging.getLogger("tensorflow").setLevel(logging.ERROR)
    logging.getLogger("absl").setLevel(logging.ERROR)
    logging.getLogger("transformers").setLevel(logging.ERROR)
    logging.getLogger("rasa").setLevel(logging.ERROR)
    io_utils.configure_colored_logging(logging.INFO)
    return logger
