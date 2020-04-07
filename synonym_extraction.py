import os
import re

input_nlu_file = './data/nlu.md'
user_nlu_file = './data/user_nlu.md'
synonym_list = []
all_synonyms = []

def detect_synonym(lines):
    """ Finds the lines in nlu.md that include the keyword "synonym:" """
    for num, line in enumerate(lines, 1):
        if 'synonym:' in line:
            synonym_list.append(num)
    return synonym_list

def find_synonym(file_link, lines, i, num):
    """ Finds all synonyms in the file, strips them, and adds it all to a single list """
    j = num[i]
    while j < len(open(file_link).readlines(  )):
        if (re.match('\r?\n', lines[j])):
            #print('line is empty:', j)
            i = i + 1
            return i
        else:
            text = lines[j]
            #print('line contains synonym:', text)
            all_synonyms.append(text[2:-1])
            j = j + 1

def collect_synonym(file_link):
    """ Takes the nlu.md files and collects the list of all synonyms and returns it """
    with open(file_link, 'r') as f:
        lines = f.readlines()
        num = detect_synonym(lines)
        for i in range(len(num)):
           find_synonym(file_link, lines, i, num)
        f.close()
        return all_synonyms

def write_synonym_to_file(lines, new_synonym, num):
    """ Takes the new synonym given by the user and writes it to a secondary file """
    with open(user_nlu_file, 'w') as f:
        lines.insert(num, new_synonym)
        lines = "".join(lines)
        f.write(lines)
        f.close()

def add_synonym(synonym_cat, new_synonym):
    """ Decides where in the file that the new synonym should be written and then calls the function to write there"""
    with open(user_nlu_file, 'r') as f:
        lines = f.readlines()
        num = detect_synonym(lines)
        f.close()
    new_synonym = '- ' + new_synonym + '\n'
    if   synonym_cat == 'find':
        write_synonym_to_file(lines, new_synonym, num[0])
    elif synonym_cat == 'move':
        write_synonym_to_file(lines, new_synonym, num[1])
    elif synonym_cat == 'pick up':
        write_synonym_to_file(lines, new_synonym, num[2])

#if __name__ == "__main__":
    #all_synonyms = collect_synonym(input_nlu_file) + collect_synonym(user_nlu_file)
    #print(all_synonyms)
    
    #synonym_cat = 'pick up'
    #new_synonym = 'TESTattachTEST'
    
    #add_synonym(synonym_cat, new_synonym)
