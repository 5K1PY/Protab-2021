from string import *
from copy import copy


def to_hash(x):
    return sum([el*2**i for i, el in enumerate(x)])


mapa = []
f = open("2b.txt")
line = f.readline().strip()

n_keys = 0 
while line != "":
    if "@" in line:
        start = (line.index("@"), len(mapa))
    for char in line:
        if char in ascii_lowercase:
            n_keys += 1
    mapa.append(list(line))
    line = f.readline().strip()

all_keys = {chr(ord("a") + i): i for i in range(26)}
found = [[{} for i in range(len(mapa[0]))] for i in range(len(mapa))]

time = 0
stack = [[start, [False]*len(all_keys)]]
new_stack = []
while True:
    print(time)
    for (x, y), keys in stack:
        point = mapa[y][x]

        if point in ascii_lowercase:
            keys[all_keys[point]] = True
            if sum(keys) == n_keys:
                print(time)
                quit()

        if to_hash(keys) in found[y][x] or (point in ascii_uppercase and keys[all_keys[point.lower()]] is False):
            continue
        found[y][x][to_hash(keys)] = True

        d_x, d_y = 1, 0
        for i in range(4):
            nx, ny = x + d_x, y + d_y
            if not (mapa[ny][nx] == "#"):
                new_stack.append([(nx, ny), keys[:]])
            d_x, d_y = -d_y, d_x

    stack = new_stack
    new_stack = []
    time += 1
