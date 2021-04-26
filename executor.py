import pickle
import random
import nltk
from collections import defaultdict

with open ('trees/' + 'seuss_trees.pickle', 'rb') as seuss_file:
    seuss_trees = pickle.load(seuss_file)

with open ('trees/' + 'thug_trees.pickle', 'rb') as thug_file:
    thug_trees = pickle.load(thug_file)

with open ('trees/' + 'thug_tokens.pickle', 'rb') as thug_file2:
    thug_tokens = pickle.load(thug_file2)

#print(thug_tokens[0][0][0])

#pick 5 in a row??
seuss_tree = random.choice(seuss_trees)

#construct cfd or big data structure dictionary by syntactical piece as the key to find words that fit. 
thug_dict = dict()
for sentence in thug_tokens:
    #print(sentence)
    for word_token in sentence:
        print(word_token)
        if word_token[1] not in thug_dict.keys():
            thug_dict[word_token[1]] = word_token[0]
        else:
            thug_dict[word_token[1]].append(word_token[0])

            #might need a nested dictionary here
            #would like each syntax option to be a dict entry with each thug word, along with the number of times it has appeared as
            #that piece of syntax
            #from here can use this dictionary to generate seuss structured young thug lyrics






""" sentence = ''
for token in (seuss_tree):
    #print(token)
    #print(token[1])
    if(token[0] in ['.', ',', '!', '?', '\'']): #does not put spaces before punctuation
        try:
            sentence += token[0] #handles nested tuples in syntax tree
        except:
            sentence += token[0][0]
    else:
        try:
            sentence += ' ' + token[0] #handles nested tuples in syntax tree
        except:
            sentence += ' ' + token[0][0]
print(sentence) """