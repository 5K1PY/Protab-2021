from string import *
from copy import copy


def to_hash(x):
    return tuple([sum([el*2**i for i, el in enumerate(x)])])


mapa = []
f = open("2f.txt")
line = f.readline().strip()
starts = []

while line != "":
    if "@" in line:
        i = 0
        while "@" in line[i:]:
            starts.append((line.index("@", i), len(mapa), "g"))
            i = line.index("@", i) + 1
    mapa.append(list(line))
    line = f.readline().strip()

all_keys = {chr(ord("a") + i): i for i in range(26)}
found = [[{} for i in range(len(mapa[0]))] for i in range(len(mapa))]

simple_pos_change = [(1, 0), (0, 1), (-1, 0), (0, -1)]
pos_change = []
for p1 in simple_pos_change:
    for p2 in simple_pos_change:
        for p3 in simple_pos_change:
            for p4 in simple_pos_change:
                pos_change.append((p1, p2, p3, p4))

time = 0
stack = [[starts, [False]*len(all_keys)]]
new_stack = []
while True:
    print(time)
    for pos, keys in stack:

        skip = False
        all_doors = True 
        for x, y, flag in pos:
            if flag == "w":
                found[y][x][to_hash(keys)] = time
                continue
            if to_hash(keys) in found[y][x] and time > found[y][x][to_hash(keys)]:
                skip = True
                break
            all_doors = False
            found[y][x][to_hash(keys)] = time

        if skip is True or all_doors is True:
            continue

        for p in pos_change:
            solution = []
            new_keys = keys[:]
            for index, (sx, sy, _) in enumerate(pos):
                x, y = sx + p[index][0], sy + p[index][1]

                point = mapa[y][x]

                if point in ascii_lowercase:
                    new_keys[all_keys[point]] = True
                    if all(new_keys):
                        print(time+1)
                        quit()

                if point in ascii_uppercase and new_keys[all_keys[point.lower()]] is False:
                    solution.append((sx, sy, "w"))
                    continue

                if point == "#":
                    solution = False
                    break

                solution.append((x, y, "g"))

            if solution is not False:
                new_stack.append((solution, new_keys))

    stack = new_stack
    new_stack = []
    time += 1
