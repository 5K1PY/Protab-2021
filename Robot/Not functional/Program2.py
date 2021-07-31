def bfs(mapa, start, mark):
    stack = [start]
    new_stack = []
    time = 0
    while len(stack):
        for start_x, start_y in stack:
            if mapa[start_y][start_x] == "#" or isinstance(mapa[start_y][start_x], int):
                continue
            mapa[start_y][start_x] = time

            d_x, d_y = 1, 0
            for i in range(4):
                x, y = start_x + d_x, start_y + d_y
                if isinstance(mapa[y][x], int) and time - mapa[y][x] > 1:
                    assert False
                if not (mapa[y][x] == "#" or isinstance(mapa[y][x], int)):
                    new_stack.append((x, y))
                d_x, d_y = -d_y, d_x

        stack = new_stack
        new_stack = []
        time += 1

    return time - 2


def nice_print(mapa):
    return ("\n".join(["".join(map(str, line)).replace("#", ".") for line in mapa]))


mapa = []
f = open("1.txt")
line = f.readline().strip()

while line != "":
    mapa.append(list(line))
    line = f.readline().strip()


print(bfs(mapa, (1, 1), 0))

f = open("1.out", "w")
f.write(nice_print(mapa))
