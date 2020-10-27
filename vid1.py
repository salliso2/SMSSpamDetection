import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

example_text = "Hello there, how are you doing today? The weather is great and Python is awesome. The sky is pinkish-blue. You should not eat cardboard."

# Split example_text by word
wordList = sent_tokenize(example_text)
print(wordList)

print()

# Split by sentence
sentList = (word_tokenize(example_text))
print(sentList)


