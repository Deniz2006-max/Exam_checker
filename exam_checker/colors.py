import json
import math
import numpy as np

color_data = json.loads(open("xkcd.json").read())
print(color_data)
def hex_to_int(s):
    s = s.lstrip("#")
    print(s)
    return int(s[:2], 16), int(s[2:4], 16), int(s[4:6], 16)


colors = dict()
for item in color_data['colors']:
    colors[item["color"]] = hex_to_int(item["hex"])

print(colors)

# finding the euclidian distance between vectors
def distance(coord1, coord2):
    # note, this is VERY SLOW, don't use for actual code

    return math.sqrt(sum([(i - j)**2 for i, j in zip(coord1, coord2)]))
print(distance([10, 1], [5, 2]))



def meanv(coords):
    # assumes every item in coords has same length as item 0
    sumv = [0] * len(coords[0])
    print(sumv)
    for item in coords:
        for i in range(len(item)):
            sumv[i] += item[i]
    mean = [0] * len(sumv)
    for i in range(len(sumv)):
        mean[i] = float(sumv[i]) / len(coords)
    return mean
print(meanv([[0, 1], [2, 2], [4, 3]]))

k = np.array([[0, 1], [2, 2], [4, 3]])

print(k.shape)
print(k[0])
def subtractv(coord1, coord2):
    return [c1 - c2 for c1, c2 in zip(coord1, coord2)]

def closest(space, coord, n=10):
    closest = []
    for key in sorted(space.keys(),
                      key=lambda x: distance(coord, space[x]))[:n]:
        closest.append(key)
    return closest

print(closest(colors, colors['red']))


print(closest(colors, subtractv(colors["purple"], colors["red"])))