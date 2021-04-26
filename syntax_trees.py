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

#thug_tokens = make_token_list(thug_sentences)
#thug_trees = make_syntax_trees(thug_sentences)
#seuss_trees = make_syntax_trees(seuss_sentences)

#pickle.dump(thug_tokens, open('trees/' + "thug_tokens.pickle", "wb" ) )
#pickle.dump(thug_trees, open( 'trees/' + "thug_trees.pickle", "wb" ) ) #close files?
#pickle.dump(seuss_trees, open('trees/' + "seuss_trees.pickle", "wb" ) )