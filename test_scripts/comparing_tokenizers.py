from utils import spacy_nlp, logging_setup

from rasa.nlu.tokenizers.whitespace_tokenizer import WhitespaceTokenizer
from rasa.nlu.tokenizers.spacy_tokenizer import SpacyTokenizer
from rasa.nlu.tokenizers.mitie_tokenizer import MitieTokenizer
from rasa.nlu.tokenizers.convert_tokenizer import ConveRTTokenizer
from rasa.nlu.tokenizers.lm_tokenizer import LanguageModelTokenizer
from rasa.nlu.utils.hugging_face.hf_transformers import HFTransformersNLP
from rasa.nlu.training_data import Message
from rasa.nlu.constants import (TEXT, SPACY_DOCS)

logger = logging_setup()

test_input = "Okay, pick up this yellow banana for me."
message = Message(test_input)

tk = WhitespaceTokenizer()
tokens = tk.tokenize(message, attribute=TEXT)
logger.info('Whitespace: {}'.format([t.text for t in tokens]))

tk = SpacyTokenizer()

message.set(SPACY_DOCS[TEXT], spacy_nlp(test_input))
tokens = tk.tokenize(message, attribute=TEXT)
logger.info('SpaCy: {}'.format([t.text for t in tokens]))

tk = MitieTokenizer()
tokens = tk.tokenize(message, attribute=TEXT)
logger.info('Mitie: {}'.format([t.text for t in tokens]))

tk = ConveRTTokenizer()
tokens = tk.tokenize(message, attribute=TEXT)
logger.info('ConveRT: {}'.format([t.text for t in tokens]))

tk = LanguageModelTokenizer()
transformers_nlp = HFTransformersNLP({"model_name": "bert"})
transformers_nlp.process(message)
tokens = tk.tokenize(message, attribute=TEXT)
logger.info('BERT: {}'.format([t.text for t in tokens]))
