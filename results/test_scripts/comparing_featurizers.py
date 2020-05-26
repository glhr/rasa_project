from utils import spacy_nlp, mitie_feature_extractor, logging_setup
from rasa.nlu.training_data import Message

from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.featurizers.dense_featurizer.spacy_featurizer import SpacyFeaturizer

from rasa.nlu.tokenizers.mitie_tokenizer import MitieTokenizer
from rasa.nlu.featurizers.dense_featurizer.mitie_featurizer import MitieFeaturizer

from rasa.nlu.tokenizers.tokenizer import Tokenizer
from rasa.nlu.tokenizers.convert_tokenizer import ConveRTTokenizer
from rasa.nlu.featurizers.dense_featurizer.convert_featurizer import ConveRTFeaturizer

from rasa.nlu.tokenizers.whitespace_tokenizer import WhitespaceTokenizer
from rasa.nlu.featurizers.sparse_featurizer.count_vectors_featurizer import CountVectorsFeaturizer

from rasa.nlu.constants import SPACY_DOCS, TEXT, DENSE_FEATURE_NAMES, TOKENS_NAMES, SPARSE_FEATURE_NAMES

logger = logging_setup()

featurizer = SpacyFeaturizer.create({}, RasaNLUModelConfig())

test_input = "Okay, pick up this yellow banana for me."
message = Message(test_input)

message.set(SPACY_DOCS[TEXT], spacy_nlp(test_input))
featurizer._set_spacy_features(message)
vecs = message.get(DENSE_FEATURE_NAMES[TEXT])
logger.info("SpaCy: {}".format(vecs.shape))

message = Message(test_input)
featurizer = MitieFeaturizer.create({}, RasaNLUModelConfig())
MitieTokenizer().process(message)
tokens = message.get(TOKENS_NAMES[TEXT])
vecs = featurizer.features_for_tokens(tokens, mitie_feature_extractor)
logger.info("Mitie: {}".format(vecs.shape))

featurizer = ConveRTFeaturizer.create({}, RasaNLUModelConfig())
tokens = ConveRTTokenizer().tokenize(message, attribute=TEXT)
tokens = Tokenizer.add_cls_token(tokens, attribute=TEXT)
message.set(TOKENS_NAMES[TEXT], tokens)
featurizer.process(message)
vecs = message.get(DENSE_FEATURE_NAMES[TEXT])
logger.info("ConveRT: {}".format(vecs.shape))
