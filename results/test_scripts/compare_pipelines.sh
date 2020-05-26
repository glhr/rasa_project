rasa test nlu \
--config \
../pipelines/pretrained_embeddings_spacy.yml \
../pipelines/supervised_embeddings.yml \
../pipelines/recommended.yml \
--nlu ../data/nlu.md \
--runs 1 --percentages 0 10 20 30
