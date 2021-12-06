from __future__ import unicode_literals
import spacy
import numpy as np
from numpy import dot
from numpy.linalg import norm
nlp = spacy.load("en_core_web_md")
doc = nlp(open("pg345.txt").read())


tokens = list(set([w.text for w in doc if w.is_alpha]))

def vec(s):
    return nlp.vocab[s].vector
def cosine(v1, v2):
    if norm(v1) > 0 and norm(v2) > 0:
        return dot(v1, v2) / (norm(v1) * norm(v2))
    else:
        return 0.0

def spacy_closest(token_list, vec_to_check, n=10):
    return sorted(token_list,
                  key=lambda x: cosine(vec_to_check, vec(x)),
                  reverse=True)[:n]

# print(spacy_closest(tokens, vec("basketball")))
def meanv(coords):
    # assumes every item in coords has same length as item 0
    sumv = [0] * len(coords[0])
    for item in coords:
        for i in range(len(item)):
            sumv[i] += item[i]
    mean = [0] * len(sumv)
    for i in range(len(sumv)):
        mean[i] = float(sumv[i]) / len(coords)
    return mean

#sentence similarity
# scoring the average vector of words for the vector of the sentence
def sentvec(s):
    sent = nlp(s)
    return meanv([w.vector for w in sent])

sentences = list(doc.sents)

def spacy_closest_sent(space, input_str, n=10):
    input_vec = sentvec(input_str)
    return sorted(space,
                  key=lambda x: cosine(np.mean([w.vector for w in x], axis=0), input_vec),
                  reverse=True)[:n]

for sent in spacy_closest_sent(sentences, "he is a relaxed man"):
    print(sent.text)
    print("---")