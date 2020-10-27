from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sentence = "This is an example showing off stop word filtration."

# A Pre-Made Set of Common Stop Words (you can append to this list if you want)
stop_words = set(stopwords.words("english"))

words = word_tokenize(example_sentence)

filtered_sentence = []

for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

print(filtered_sentence)


# Faster Way To Do The Above - Generator Expression (I think)
filtered_sentence = [w for w in words if not w in stop_words]
