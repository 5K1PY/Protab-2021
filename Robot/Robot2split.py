from string import *


def split_maze(name):
    mapa = []
    f = open(f"{name}.txt")
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

    f.close()

    # for y in range(len(mapa)):
    #     for x in range(len(mapa[0])):
    #             if mapa[y][x] in ascii_uppercase:
    #                 mapa[y][x] = " "

    for i in range(4):
        f = open(f"{name}-{i}.txt", "w")
        if i == 0:
            map_part = ["".join(mapa[i][:len(mapa[0])//2+1]) for i in range(len(mapa)//2+1)]
        if i == 1:
            map_part = ["".join(mapa[i][len(mapa[0])//2:]) for i in range(len(mapa)//2+1)]
        if i == 2:
            map_part = ["".join(mapa[i][:len(mapa[0])//2+1]) for i in range(len(mapa)//2, len(mapa))]
        if i == 3:
            map_part = ["".join(mapa[i][len(mapa[0])//2:]) for i in range(len(mapa)//2, len(mapa))]
        f.write("\n".join(map_part))
        f.close()
