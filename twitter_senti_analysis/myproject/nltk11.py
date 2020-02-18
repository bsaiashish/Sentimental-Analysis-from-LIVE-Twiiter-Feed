from nltk.tokenize import sent_tokenize, word_tokenize
example_text="HEllo Mr. Smith, there, how are you doing today? The weather is great and python is awesome. The sky is pinkish blue you should not eat glue"
print (sent_tokenize(example_text))
print (word_tokenize(example_text))

for i in word_tokenize(example_text):
    print (i)

