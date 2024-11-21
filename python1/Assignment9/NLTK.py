import nltk
from nltk.tokenize import word_tokenize

# Download required NLTK data
nltk.download('punkt')

# Example text
text = "Hello, how are you doing today?"

# Tokenize the text into words
tokens = word_tokenize(text)
print("Tokens:", tokens)

# Perform POS tagging (part of speech tagging)
pos_tags = nltk.pos_tag(tokens)
print("POS Tags:", pos_tags)
