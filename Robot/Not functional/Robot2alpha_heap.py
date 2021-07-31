from string import *
from copy import copy
from heapq import *

def to_hash(x):
    return tuple([sum([el*2**i for i, el in enumerate(x)])])

def search(mapa, start, keys):
    time = 0
    stack = [start]
    new_stack = []
    found = [[False]*len(mapa[0]) for i in range(len(mapa))]

    to_do = len(keys) - sum(keys)
    res = 0
    while len(stack):
        for start_x, start_y in stack:
            if found[start_y][start_x] is True:
                continue
            found[start_y][start_x] = True

            if mapa[start_y][start_x] in ascii_lowercase:
                to_do -= 1
                res += time

            delta_x, delta_y = 1, 0
            for i in range(4):
                x, y = start_x + delta_x, start_y + delta_y

                point = mapa[y][x]
                if point != "#":
                    new_stack.append((x, y))

                delta_x, delta_y = -delta_y, delta_x

        time += 1
        stack = new_stack
        new_stack = []
    return res


mapa = []
f = open("2fO.txt")
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

t = 0
time = 0
stack = [[0, 0, starts, [False]*len(all_keys)]]
while True:
    _, time, pos, keys = heappop(stack)
    if t < time:
        t = time
        print(time)

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
            bonus_time = 0
            for x, y, _ in solution:
                bonus_time += search(mapa, (x, y), new_keys)
            heappush(stack, [time+bonus_time+1, time+1, solution, new_keys])
