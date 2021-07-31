from string import *
from copy import copy


def to_hash(x):
    return tuple([sum([el*2**i for i, el in enumerate(x)])])

def nice_print(mapa, found):
    return ["".join(["1" if len(found[y][x]) > 0 and mapa[y][x] == " " else mapa[y][x] for x in range(len(mapa[0]))]) for y in range(len(mapa))]

mapa = []
f = open("2b.txt")
line = f.readline().strip()
starts = []

while line != "":
    if "@" in line:
        i = 0
        while "@" in line[i:]:
            starts.append((line.index("@", i), len(mapa)))
            i = line.index("@", i) + 1
    mapa.append(list(line))
    line = f.readline().strip()

n_keys = 26
all_keys = {chr(ord("a") + i): i for i in range(n_keys)}
found = [[{} for i in range(len(mapa[0]))] for i in range(len(mapa))]

time = 0

stored = {chr(ord("a") + i): [] for i in range(n_keys)}
ready = {chr(ord("a") + i): [] for i in range(n_keys)}
stored["_"] = []
ready["_"] = []
stack = [[start, [False]*len(all_keys), [i]] for i, start in enumerate(starts)]
new_stack = []

bindings = {}
max_bindings = {}
binded = {}

while True:
    print(time, max(map(lambda x: sum(x[1]), stack)))
    changed = False
    for (start_x, start_y), keys, binding in stack:
        if to_hash(keys) in found[start_y][start_x]:
            continue
        found[start_y][start_x][to_hash(keys)] = time

        if mapa[start_y][start_x] in ascii_lowercase:
            keys[all_keys[mapa[start_y][start_x]]] = True
            if all(keys):
                print(time)
                quit()
            changed = True
            ready[mapa[start_y][start_x]].append([(start_x, start_y), keys[:], binding])

            # stored["_"].append([(start_x, start_y), keys[:], binding])
            # ready["_"].append([(start_x, start_y), keys[:], binding])
            # binded[(start_x, start_y), (start_x, start_y), to_hash(keys), to_hash(keys), tuple(binding), tuple(binding)] = True

        dx, dy = 1, 0
        for i in range(4):
            x, y = start_x + dx, start_y + dy
            if mapa[y][x] in ascii_uppercase and keys[all_keys[mapa[y][x].lower()]] is False:
                changed = True
                stored[mapa[y][x].lower()].append([(x, y), keys[:], binding])
            elif mapa[y][x] != "#":
                new_stack.append([(x, y), keys[:], binding])
            dx, dy = -dy, dx

    if changed:
        for key in stored:
            if len(stored[key]) == 0 or len(ready[key]) == 0:
                continue
            for s_poz, s_keys, s_bind in stored[key]:
                for r_poz, r_keys, r_bind in ready[key]:
                    # is bindable

                    if (s_poz, r_poz, to_hash(s_keys), to_hash(r_keys), tuple(s_bind), tuple(r_bind)) in binded:
                        continue
                    binded[(s_poz, r_poz, to_hash(s_keys), to_hash(r_keys), tuple(s_bind), tuple(r_bind))] = True
                    if key == "_":
                        binded[(r_poz, s_poz, to_hash(r_keys), to_hash(s_keys), tuple(r_bind), tuple(s_bind))] = True

                    bindable = True
                    if s_bind[0] == r_bind[0]:
                        continue

                    if len(s_bind) >= len(r_bind):
                        shorter = r_bind
                        longer = s_bind
                    else:
                        shorter = s_bind
                        longer = r_bind

                    for i in range(1, len(shorter)):
                        if s_bind[i] != r_bind[i]:
                            bindable = False
                            break
                    # for i in range(len(shorter), len(longer)):
                    #     if longer[i][1] == shorter[0]:
                    #         bindable = False
                    #         break
                    if not bindable:
                        continue

                    if key == "_":
                        if all([s_keys[i] or r_keys[i] for i in range(len(keys))]):
                            print(time)
                            quit()
                        else:
                            continue

                    b = max_bindings
                    for el in longer[1:]:
                        b = b[el[0]]
                    tail = (len(b), r_bind[0])
                    b[tail[0]] = {}

                    new_bind = [s_bind[0]] + longer[1:] + [tail]
                    new_keys = [s_keys[i] or r_keys[i] for i in range(len(keys))]
                    new_stack.append([s_poz, new_keys, new_bind])

    stack = new_stack
    new_stack = []
    time += 1
