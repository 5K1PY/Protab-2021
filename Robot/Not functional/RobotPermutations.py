from copy import copy, deepcopy
from itertools import permutations
from math import inf
from string import ascii_lowercase

def fact(x):
    res = 1
    for i in range(2, x+1):
        res *= i
    return res

def key(point):
    return isinstance(point, str) and point in ascii_lowercase and point.lower() == point


def unlock(point, keys):
    return isinstance(point, str) and point.lower() in keys


def older(point, mark):
    return isinstance(point, int) and point < mark


def search(mapa, start, end, keys, mark):
    time = 0
    stack = [start]
    new_stack = []

    while len(stack):
        for start_x, start_y in stack:
            if mapa[start_y][start_x] == end:
                return (start_x, start_y, time)
            if not key(mapa[start_y][start_x]):
                mapa[start_y][start_x] = mark
            delta_x, delta_y = 1, 0
            for i in range(4):
                x, y = start_x + delta_x, start_y + delta_y
                if 0 <= x <= len(mapa[0]) and 0 <= y <= len(mapa):
                    point = mapa[y][x]
                    if point == " " or unlock(point, keys) or key(point) or older(point, mark):
                        new_stack.append((x, y))

                delta_x, delta_y = -delta_y, delta_x

        time += 1
        stack = new_stack
        new_stack = []
    return None


f = open("1.txt")

mapa = []
line = f.readline().strip()

all_keys = {}

while line != "":
    mapa.append(list(line))
    for char in line:
        if char not in ("#", "@", " ") and key(char):
            all_keys[char] = True
        elif char == "@":
            bot = (line.index("@"), len(mapa)-1)
    line = f.readline().strip()

min_time = inf
index = 1
all_permutations = permutations(all_keys.keys())
for p in all_permutations:
    mark = 0
    start = copy(bot)
    new_map = deepcopy(mapa)
    time = 0
    next_key = 0
    keys = {}

    while next_key < len(p):
        res = search(new_map, start, p[next_key], keys, mark)
        if res is None:
            break

        start = res[0], res[1]
        time += res[2]
        keys[p[next_key]] = True
        next_key += 1
        mark += 1

    print(f"{index} / {fact(len(all_keys))}: {min_time}")
    index += 1

    if res is None:
        continue
    
    min_time = min(time, min_time)


print(min_time)
