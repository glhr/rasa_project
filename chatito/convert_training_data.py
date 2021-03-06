from rasa.nlu.training_data import load_data

# This re-uses the Rasa NLU converters code to turn a JSON Rasa NLU training
# file into MD format and save it

# Assumes you have Rasa NLU installed :-)

# If you want other options, look at the NLU code to work out how to handle them

# USE AT YOUR OWN RISK

files = {
    './commands.json': '../data/auto-generated/commands.md',
    './clarification.json': '../data/auto-generated/clarification.md',
}
# *******************************************************
# TAKE CARE: output_md_file is overwritten automatically
# *******************************************************

for file in files.keys():
    output_md_file = files[file]
    input_training_file = file
    with open(output_md_file,'w') as f:
        f.write(load_data(input_training_file).as_markdown())
