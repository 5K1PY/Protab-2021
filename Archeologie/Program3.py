from heapq import *

def nice_print(mapa):
    print("\n".join(["".join(map(str, line)).replace("#", ".") for line in mapa]))

mapa = []
f = open("3b.txt")
line = f.readline().strip()

while line != "":
    mapa.append(list(line))
    line = f.readline().strip()

heap = [(0, 1, 1)]
while True:
    time, x, y = heappop(heap)

    if x == len(mapa[0]) - 2 and y == len(mapa) - 2:
        break

    if isinstance(mapa[y][x], int):
        continue

    mapa[y][x] = time

    d_x, d_y = 1, 0
    for i in range(4):
        nx, ny = x + d_x, y + d_y
        if not (0 <= nx < len(mapa[0]) and 0 <= ny < len(mapa)):
            continue
        if not isinstance(mapa[ny][nx], int):
            if mapa[ny][nx] == "#":
                heappush(heap, (time + 11, nx, ny))
            if mapa[ny][nx] == " ":
                heappush(heap, (time + 1, nx, ny))
        d_x, d_y = -d_y, d_x

print(time)
