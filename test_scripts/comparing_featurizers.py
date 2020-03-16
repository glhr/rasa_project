from utils import spacy_nlp, logging_setup
from rasa.nlu.training_data import Message
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.featurizers.dense_featurizer.spacy_featurizer import SpacyFeaturizer
from rasa.nlu.constants import SPACY_DOCS, TEXT, DENSE_FEATURE_NAMES

logger = logging_setup()

featurizer = SpacyFeaturizer.create({}, RasaNLUModelConfig())

test_input = "Okay, pick up this yellow banana for me."
message = Message(test_input)
message.set(SPACY_DOCS[TEXT], spacy_nlp(test_input))
featurizer._set_spacy_features(message)
vecs = message.get(DENSE_FEATURE_NAMES[TEXT])
logger.info("SpaCy: {}".format(vecs.shape))
