from rasa.nlu.tokenizers.whitespace_tokenizer import WhitespaceTokenizer
from rasa.nlu.tokenizers.spacy_tokenizer import SpacyTokenizer
from rasa.nlu.tokenizers.mitie_tokenizer import MitieTokenizer
from rasa.nlu.tokenizers.convert_tokenizer import ConveRTTokenizer
from rasa.nlu.tokenizers.lm_tokenizer import LanguageModelTokenizer
from rasa.nlu.utils.hugging_face.hf_transformers import HFTransformersNLP

from rasa.nlu.training_data import Message

from rasa.nlu.utils.spacy_utils import SpacyNLP

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
print('Whitespace:',[t.text for t in tokens])
#
# tk = SpacyTokenizer()
# # message.set(SPACY_DOCS[TEXT], spacy_nlp(test_input))
# tokens = tk.tokenize(message, attribute=TEXT)
# print([t.text for t in tokens])

tk = MitieTokenizer()
tk.process(message)
tokens = tk.tokenize(message, attribute=TEXT)
print('Mitie:',[t.text for t in tokens])

tk = ConveRTTokenizer()
tokens = tk.tokenize(message, attribute=TEXT)
print('ConveRT:',[t.text for t in tokens])

transformers_nlp = HFTransformersNLP({"model_name": "bert"})
lm_tokenizer = LanguageModelTokenizer()
message = Message.build(text=test_input)
transformers_nlp.process(message)
tokens = lm_tokenizer.tokenize(message, TEXT)
print('BERT:',[t.text for t in tokens])
