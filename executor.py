import pickle
import random

with open ('trees/' + 'seuss_trees.pickle', 'rb') as seuss_file:
    seuss_trees = pickle.load(seuss_file)
#seuss_trees = pickle.load( open('trees/' + 'seuss_trees.pickle', 'rb'))
with open ('trees/' + 'thug_trees.pickle', 'rb') as thug_file:
    thug_trees = pickle.load(thug_file)
#thug_trees = pickle.load(open('trees/' + 'thug_trees.pickle', 'rb'))

#print(thug_trees[308][0][0])

seuss_tree = random.choice(seuss_trees)
print(seuss_tree)
sentence = ''
for token in (seuss_tree):
    print(token)
    print(token[0])
    if(token[0] in ['.', ',', '!', '?']):
        try:
            sentence += token[0]
        except:
            sentence += token[0][0]
    else:
        try:
            sentence += ' ' + token[0]
        except:
            sentence += ' ' + token[0][0]
print(sentence)