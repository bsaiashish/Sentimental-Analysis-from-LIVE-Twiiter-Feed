from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()

example_words = ["python","pythoning","pythoner","pythoned","pythonly"]

'''
for w in example_words:
    print(ps.stem(w))
'''

new_text="it id very imop to be pythonly while pythoning to be a true pythoner and be pythoned"

words = word_tokenize(new_text)

for w in words:
    print(ps.stem(w))
