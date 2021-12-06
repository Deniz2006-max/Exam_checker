import pandas as pd
import matplotlib.pyplot as plt
import re

dataset = pd.read_csv("tweets.csv", encoding="ISO-8859-1")
print(dataset.head(10))
def gen_freq(text):
    word_list = []

    for tw_word in text.split():
        word_list.extend(tw_word)

    word_freq = pd.Series(word_list).value_counts()
    return word_freq[:20]

# text clearing
Stopwords = {'has', 'who', 'would', 'otherwise', 'each', 'just', 'it', 'out', "can't", 'or', 'however', 'have', 'any',
             'from', "won't", 'in', 'how', 'been', 'there', "you're", 'most', 'him', "shan't", "she's", "she'd", 'at',
             'did', 'r', 'also', 'after', 'which', 'he', "aren't", 'having', "why's", "wasn't", 'other', 'them',
             "couldn't", 'herself', 'they', "you'd", 'than', "it's", 'theirs', "they're", 'am', 'on', 'what',
             'should', 'yourself', 'up', 'same', 'cannot', "isn't", "how's", 'only', 'hers', 'then', "they'll",
             'with', 'you', 'for', 'myself', 'very', "we're", 'my', 'all', 'over', 'while', "you've", 'during',
             "that's", 'being', "i'm", 'why', 'nor', 'down', 'your', 'her', 'ought', 'ours', 'again', "don't",
             'until', 'those', 'ourselves', "he'd", 'could', "hadn't", 'against', 'i', "there's", 'no', 'himself',
             'about', 'since', 'as', 'below', "wouldn't", 'that', 'me', 'whom', "you'll", 'she', 'like', "who's",
             'so', 'the', 'between', 'shall', 'more', 'too', 'such', 'themselves', "shouldn't", 'our', "we've",
             'do', 'further', 'these', 'few', 'get', 'yourselves', 'are', 'here', "weren't", "hasn't", 'above',
             "we'd", 'and', 'http', 'where', 'into', 'to', 'www', "i'd", 'we', 'but', 'ever', "haven't", 'own',
             'not', 'off', "mustn't", 'else', 'was', 'a', 'his', 'of', 'this', 'k', 'is', 'once', 'by', "what's",
             'if', "she'll", 'itself', "we'll", "where's", "he'll", 'both', 'its', 'some', 'com', 'be', "let's", 'through', 'were', 'had', "when's", "he's", 'an', 'their', 'doing',
             'does', "they'd", 'yours', "here's", "i'll", 'can', 'under', "didn't", "i've", "they've", 'because', 'before', "doesn't", 'when'}
def clean(text):

    text = re.sub("RT", "", text)
    text = re.sub("&amp:", " &", text)

    text = re.sub(r"[?.-;:,#@]", "", text)
    text = text.lower()
    return text

text = dataset.text.apply(lambda x: clean(x))
word_freq = gen_freq(text.str) *100
word_freq = word_freq.drop(labels=Stopwords, errors="ignore")
print(word_freq)