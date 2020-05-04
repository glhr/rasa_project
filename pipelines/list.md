### Recommended

If your training data is in English, a good starting point is the following pipeline:
```
language: "en"

pipeline:
  - name: ConveRTTokenizer
  - name: ConveRTFeaturizer
  - name: RegexFeaturizer
  - name: LexicalSyntacticFeaturizer
  - name: CountVectorsFeaturizer
  - name: CountVectorsFeaturizer
    analyzer: "char_wb"
    min_ngram: 1
    max_ngram: 4
  - name: DIETClassifier
    epochs: 100
  - name: EntitySynonymMapper
  - name: ResponseSelector
    epochs: 100
  ```

### pretrained_embeddings_spacy

The advantage of pretrained_embeddings_spacy pipeline is that if you have a training example like: “I want to buy apples”, and Rasa is asked to predict the intent for “get pears”, your model already knows that the words “apples” and “pears” are very similar. This is especially useful if you don’t have enough training data.

To use the pretrained_embeddings_spacy template, use the following configuration:

```
language: "en"
pipeline:
- name: "SpacyNLP"
- name: "SpacyTokenizer"
- name: "SpacyFeaturizer"
- name: "RegexFeaturizer"
- name: "CRFEntityExtractor"
- name: "EntitySynonymMapper"
- name: "SklearnIntentClassifier"
```
