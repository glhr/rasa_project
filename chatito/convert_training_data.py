from rasa.nlu.training_data import load_data

# This re-uses the Rasa NLU converters code to turn a JSON Rasa NLU training
# file into MD format and save it

# Assumes you have Rasa NLU installed :-)

# If you want other options, look at the NLU code to work out how to handle them

# USE AT YOUR OWN RISK

input_training_file = './find.json'

# *******************************************************
# TAKE CARE: output_md_file is overwritten automatically
# *******************************************************

output_md_file = '../data/nlu/find.md'

with open(output_md_file,'w') as f:
    f.write(load_data(input_training_file).as_markdown())
