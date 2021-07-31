from heapq import *


def nice_print(mapa):
    print("\n".join(["".join(map(str, line)).replace("#", ".") for line in mapa]))


mapa = []
f = open("4b.txt")
line = f.readline().strip()

while line != "":
    mapa.append(list(line))
    line = f.readline().strip()

heap = [(0, 1, 1)]
while True:
    time, x, y = heappop(heap)

    if x == len(mapa[0]) - 6 and y == len(mapa) - 6:
        break

    if isinstance(mapa[y][x], int):
        continue

    mapa[y][x] = time

    d_x, d_y = 1, 0
    for i in range(4):
        nx, ny = x + d_x, y + d_y
        if not (0 <= nx < len(mapa[0]) - 4 and 0 <= ny < len(mapa) - 4):
            continue
        if not isinstance(mapa[ny][nx], int):
            drill = time + 1

            if (d_x, d_y) == (1, 0):
                for c_y in range(y, y+5):
                    drill += 10 if mapa[c_y][x + 5] == "#" else 0
            elif (d_x, d_y) == (-1, 0):
                for c_y in range(y, y+5):
                    drill += 10 if mapa[c_y][x - 1] == "#" else 0
            elif (d_x, d_y) == (0, 1):
                for c_x in range(x, x+5):
                    drill += 10 if mapa[y + 5][c_x] == "#" else 0
            elif (d_x, d_y) == (0, -1):
                for c_x in range(x, x+5):
                    drill += 10 if mapa[y - 1][c_x] == "#" else 0

            heappush(heap, (drill, nx, ny))

        d_x, d_y = -d_y, d_x

print(time)
