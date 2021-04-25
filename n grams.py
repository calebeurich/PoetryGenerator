import nltk
from nltk.util import ngrams
import re
import random


with open('lyrics/' + 'Young Thug' + '.txt', encoding='utf-8') as f:
    lines = f.read()


#later learn how to make this preserve apostrophes too for words like "I'm" or "don't"
#cleaned_sentences = [re.sub(r"[^a-zA-Z0-9]+", ' ', k) for k in lines.split("\n")]
#print(cleaned_sentences)

data = lines.split()

""" def extract_ngrams(data, num):
    n_grams = ngrams(nltk.word_tokenize(data), num)
    return [ ' '.join(grams) for grams in n_grams] """

""" print("1-gram: ", extract_ngrams(data, 1))
print("2-gram: ", extract_ngrams(data, 2))
print("3-gram: ", extract_ngrams(data, 3))
 """

bigrams = nltk.bigrams(data)
cfd = nltk.ConditionalFreqDist(bigrams)

# pick a random word from the corpus to start with
word = random.choice(data)
# generate 15 more words

print(cfd['cups']['stuffed'])# ex

""" for i in range(15):
    print(word)
    if word in cfd:
        word = random.choice(list(cfd[word].keys())) #I don't think this chooses words proportional to their number of appearances
    else:
        break """