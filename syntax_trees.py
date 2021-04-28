'''
Caleb Eurich
CSCI 3725
M6
4/27/2021

This file maxes syntax trees for the Dr Seuss lines and saves them to a pickle file for later use. It also creates a token list
for Young Thug lyrics then creates and pickles a dictionary with syntactical tokens as keys and lyrics as values. The amount of words
as values is proportional to their uses, allowing for an easy bag of words approach later. In order to generate and pickle 
these data structures, one must uncomment the last 8 lines of code at the bottom.

Bugs: may cause some leak by not closing files when pickling. I am unsure how to fix this issue with the pickle structure
 or if it is a real issue.
'''

from nltk import tokenize
from nltk import tag
from nltk import chunk
import pickle

with open('lyrics/' + 'Young Thug' + '.txt', encoding='utf-8') as f:
    thug_lines = f.read()
thug_sentences = thug_lines.splitlines()

with open('lyrics/' + 'cat in the hat' + '.txt', encoding='utf-8') as f:
    seuss_lines = f.read()
seuss_sentences = seuss_lines.splitlines()


"""
make_syntax_trees creates a list of syntax trees based on input sentences using NLTK

@param sentences: a list of sentences from the input text file
@return trees: list of syntax trees based on given sentences
"""
def make_syntax_trees(sentences):
    trees = []
    i = 0 #to count where the program is at
    for sentence in sentences:
        print(i)
        words = tokenize.word_tokenize(sentence)
        tagged_sentence = tag.pos_tag(words)
        tree = chunk.ne_chunk(tagged_sentence)
        trees.append(tree)
        i+=1
    return trees


"""
make_token_list creates a list of word, token lines based on input sentences using NLTK

@param sentences: a list of sentences from the input text file
@return token_list: list of tokens and words based on given sentences
"""
def make_token_list(sentences):
    token_list = []
    i = 0 #to count where the program is at
    for sentence in sentences:
        print(i)
        words = tokenize.word_tokenize(sentence)
        tagged_sentence = tag.pos_tag(words)
        token_list.append(tagged_sentence)
        i+=1
    return token_list


"""
create_dict creates a dictionary keyed by syntax token with values of words

@param tokens: a list of token and word lines from the input text file and make_token_list
@return final_dict: dictionary keyed by syntax tokens with values of song lyric words
"""
def create_dict(tokens):
    final_dict = dict()
    for sentence in tokens:
        #print(sentence)
        for word_token in sentence:
            #print(word_token)
            if word_token[1] not in final_dict.keys():
                final_dict[word_token[1]] = [word_token[0]]
            else:
                final_dict[word_token[1]].append(word_token[0])
    return final_dict

#thug_tokens = make_token_list(thug_sentences)
#thug_dict = create_dict(thug_tokens)
#thug_trees = make_syntax_trees(thug_sentences)
#seuss_trees = make_syntax_trees(seuss_sentences)

#pickle.dump(thug_dict, open('pickles/' + "thug_dict.pickle", "wb" ) )
#pickle.dump(thug_trees, open( 'pickles/' + "thug_trees.pickle", "wb" ) ) #unsure if you need to close files with pickle
#pickle.dump(seuss_trees, open('pickles/' + "seuss_trees.pickle", "wb" ) )