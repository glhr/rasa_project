import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import logging
import rasa.utils.common
import rasa.cli.utils as cli_utils
import rasa.utils.io as io_utils

logger = logging.getLogger(__name__)

logging.getLogger("tensorflow").setLevel(logging.ERROR)
logging.getLogger("absl").setLevel(logging.ERROR)
logging.getLogger("transformers").setLevel(logging.ERROR)
logging.getLogger("rasa").setLevel(logging.ERROR)
io_utils.configure_colored_logging(logging.INFO)

from rasa.nlu.tokenizers.whitespace_tokenizer import WhitespaceTokenizer
from rasa.nlu.tokenizers.spacy_tokenizer import SpacyTokenizer
from rasa.nlu.tokenizers.mitie_tokenizer import MitieTokenizer
from rasa.nlu.tokenizers.convert_tokenizer import ConveRTTokenizer
from rasa.nlu.tokenizers.lm_tokenizer import LanguageModelTokenizer
from rasa.nlu.utils.hugging_face.hf_transformers import HFTransformersNLP
from rasa.nlu.utils.spacy_utils import SpacyNLP

from rasa.nlu.training_data import Message

from rasa.nlu.constants import (
    CLS_TOKEN,
    TEXT,
    SPACY_DOCS,
    INTENT,
    RESPONSE,
    TOKENS_NAMES,
)

test_input = "Okay, pick up this yellow banana for me."
message = Message(test_input)

tk = WhitespaceTokenizer()
tk.process(message)
tokens = message.get(TOKENS_NAMES[TEXT])
logger.info('Whitespace: {}'.format([t.text for t in tokens]))
#
# tk = SpacyTokenizer()
# # message.set(SPACY_DOCS[TEXT], spacy_nlp(test_input))
# tokens = tk.tokenize(message, attribute=TEXT)
# print([t.text for t in tokens])

tk = MitieTokenizer()
tk.process(message)
tokens = tk.tokenize(message, attribute=TEXT)
logger.info('Mitie: {}'.format([t.text for t in tokens]))

tk = ConveRTTokenizer()
tokens = tk.tokenize(message, attribute=TEXT)
logger.info('ConveRT: {}'.format([t.text for t in tokens]))

transformers_nlp = HFTransformersNLP({"model_name": "bert"})
lm_tokenizer = LanguageModelTokenizer()
message = Message.build(text=test_input)
transformers_nlp.process(message)
tokens = lm_tokenizer.tokenize(message, TEXT)
logger.info('BERT: {}'.format([t.text for t in tokens]))
