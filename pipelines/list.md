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

The pipeline contains the ConveRTFeaturizer that provides pre-trained word embeddings of the user utterance. Pre-trained word embeddings are helpful as they already encode some kind of linguistic knowledge. For example, if you have a sentence like “I want to buy apples” in your training data, and Rasa is asked to predict the intent for “get pears”, your model already knows that the words “apples” and “pears” are very similar. This is especially useful if you don’t have enough training data. The advantage of the ConveRTFeaturizer is that it doesn’t treat each word of the user message independently, but creates a contextual vector representation for the complete sentence. However, ConveRT is only available in English.

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

### supervised_embeddings

The advantage of the supervised_embeddings pipeline is that your word vectors will be customised for your domain. For example, in general English, the word “balance” is closely related to “symmetry”, but very different to the word “cash”. In a banking domain, “balance” and “cash” are closely related and you’d like your model to capture that. This pipeline doesn’t use a language-specific model, so it will work with any language that you can tokenize (on whitespace or using a custom tokenizer).

You can read more about this topic in this blog post: https://medium.com/rasa-blog/supervised-word-vectors-from-scratch-in-rasa-nlu-6daf794efcd8

```
language: "en"

pipeline:
- name: "WhitespaceTokenizer"
- name: "RegexFeaturizer"
- name: "CRFEntityExtractor"
- name: "EntitySynonymMapper"
- name: "CountVectorsFeaturizer"
- name: "CountVectorsFeaturizer"
  analyzer: "char_wb"
  min_ngram: 1
  max_ngram: 4
- name: "EmbeddingIntentClassifier"
```
