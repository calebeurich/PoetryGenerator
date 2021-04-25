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

thug_trees = make_syntax_trees(thug_sentences)
seuss_trees = make_syntax_trees(seuss_sentences)

pickle.dump(thug_trees, open( 'trees/' + "thug_trees.pickle", "wb" ) )
pickle.dump(seuss_trees, open('trees/' + "seuss_trees.pickle", "wb" ) )