from copy import copy, deepcopy
from itertools import permutations
from math import inf
from string import *

def fact(x):
    res = 1
    for i in range(2, x+1):
        res *= i
    return res


def key(point):
    return isinstance(point, str) and point in ascii_lowercase


def door(point):
    return isinstance(point, str) and point in ascii_uppercase


def older(point, mark):
    return isinstance(point, int) and point < mark


def search(mapa, start):
    time = 0
    stack = [(start, set(["start"]))]
    searched = [[False]*len(mapa[0]) for i in range(len(mapa))]
    new_stack = []

    while len(stack):
        for (start_x, start_y), keys in stack:
            if searched[start_y][start_x] is not False:
                continue
            searched[start_y][start_x] = (keys, time)
            delta_x, delta_y = 1, 0
            for i in range(4):
                x, y = start_x + delta_x, start_y + delta_y
                if 0 <= x <= len(mapa[0]) and 0 <= y <= len(mapa):
                    point = mapa[y][x]
                    if (point in (" ", "@") or key(point)) and searched[start_y][start_x] is not False:
                        new_stack.append(((x, y), keys))
                    elif door(point) and searched[start_y][start_x] is not False:
                        new_keys = copy(keys)
                        new_keys.add(point.lower())
                        new_stack.append(((x, y), new_keys))

                delta_x, delta_y = -delta_y, delta_x

        time += 1
        stack = new_stack
        new_stack = []

    return searched


f = open("1.txt")

mapa = []
line = f.readline().strip()

all_keys = {}

while line != "":
    mapa.append(list(line))
    for char in line:
        if char not in ("#", "@", " ") and key(char):
            all_keys[char] = (line.index(char), len(mapa)-1)
        elif char == "@":
            bot = (line.index("@"), len(mapa)-1)
    line = f.readline().strip()

 
access = [[None]*(len(all_keys.keys())+1) for i in range(len(all_keys.keys())+1)]
keys = ["start"] + list(sorted(all_keys.keys()))

all_keys["start"] = bot

for i1 in range(len(keys)):
    result = search(mapa, all_keys[keys[i1]])
    for i2 in range(len(keys)):
        x, y = all_keys[keys[i2]]
        access[i1][i2] = result[y][x]

min_time = inf
now_keys = [[0, 1], [1, len(keys)]]  # key_num, max_num
true_keys = set([0])
while len(now_keys) > 0:
    last = now_keys[-1]

    if last[0] == last[1]:
        true_keys.remove(now_keys[-1][0])
        now_keys.pop()
        true_keys.remove(now_keys[-1][0])
        now_keys[-1][0] += 1
        continue

    t = {keys[el] for el in true_keys}
    while last[0] < len(keys) and (last[0] in true_keys or not access[now_keys[-2][0]][last[0]][0].issubset(t)):
        last[0] += 1

    while last[0] >= len(keys):
        now_keys.pop()
        if len(now_keys) == 0:
            break
        true_keys.remove(now_keys[-1][0])
        now_keys[-1][0] += 1
        continue

    if len(now_keys) == 0:
        break

    if len(now_keys) == len(keys):
        time = 0
        for i in range(len(now_keys)-1):
            time += access[now_keys[i][0]][now_keys[i+1][0]][1]
        min_time = min(min_time, time)

        now_keys.pop()
        true_keys.remove(now_keys[-1][0])
        now_keys[-1][0] += 1
        continue

    true_keys.add(last[0])
    now_keys.append([1, len(keys)])

print(min_time)
