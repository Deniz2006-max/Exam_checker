from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
import transformers
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
#tokenization
text = "Hi john, How are you doing ? I will be travelling to your city."

tokens = word_tokenize(text)
print(pos_tag(tokens))
print(sent_tokenize(text))

#stemming
# stemmer = PorterStemmer()
# print(stemmer.stem("loving"))

#lemmatizing
lemm = WordNetLemmatizer()

print(lemm.lemmatize("took",pos="v"))

#getting synonyms

print(wordnet.synsets("good"))