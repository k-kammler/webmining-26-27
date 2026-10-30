import nltk
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

# nltk.download('stopwords')
# nltk.download('punkt_tab')

text = "Dies ist ein Beispieltext, der zur Demonstration der Tokenisierung geeignet ist."

# Tokenization
tokens = word_tokenize(text.lower())

# Remove stop words
german_stopwords = set(stopwords.words('german'))
filtered_tokens = [token for token in tokens if token.isalpha() and token not in german_stopwords]

# Generate 3-grams
trigrams = list(ngrams(tokens, 3))

# Frequency Distribution
freq_dist = FreqDist(tokens)

print("Tokens:", tokens)
print("Filtered Tokens:", filtered_tokens)
print("3-Grams:", trigrams)
print("Frequency Distribution:", freq_dist.most_common())