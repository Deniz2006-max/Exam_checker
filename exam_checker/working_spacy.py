import spacy
import json
import math
import numpy as np

nlp = spacy.load('en_core_web_sm')


color_data = json.loads(open("xkcd.json").read())

def hex_to_int(s):
    s = s.lstrip("#")
    return int(s[:2], 16), int(s[2:4], 16), int(s[4:6], 16)


colors = dict()
for item in color_data['colors']:
    colors[item["color"]] = hex_to_int(item["hex"])



# finding the euclidian distance between vectors
def distance(coord1, coord2):
    # note, this is VERY SLOW, don't use for actual code

    return math.sqrt(sum([(i - j)**2 for i, j in zip(coord1, coord2)]))



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

def subtractv(coord1, coord2):
    return [c1 - c2 for c1, c2 in zip(coord1, coord2)]

def closest(space, coord, n=10):
    closest = []
    for key in sorted(space.keys(),
                      key=lambda x: distance(coord, space[x]))[:n]:
        closest.append(key)
    return closest
doc = nlp(open("pg345.txt").read())
# use word.lower_ to normalize case
drac_colors = [colors[word.lower_] for word in doc if word.lower_ in colors]
avg_color = meanv(drac_colors)
print(closest(colors,avg_color))