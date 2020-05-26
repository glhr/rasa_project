rasa train core -c eval_stories/keras.yml eval_stories/keras_max10.yml eval_stories/keras_epochs100.yml \
  -d domain.yml -s eval_stories/stories --out eval_stories/comparison_models --runs 3 \
  --percentages 50
