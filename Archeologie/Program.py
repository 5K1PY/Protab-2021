def bfs(mapa, start, mark):
    stack = [start]
    new_stack = []
    while len(stack):
        for start_x, start_y in stack:
            if mapa[start_y][start_x] == mark:
                continue
            mapa[start_y][start_x] = mark

            d_x, d_y = 1, 0
            for i in range(4):
                x, y = start_x + d_x, start_y + d_y
                if mapa[y][x] not in (mark, "#"):
                    new_stack.append((x, y))
                d_x, d_y = -d_y, d_x

        stack = new_stack
        new_stack = []


def nice_print(mapa):
    print("\n".join(["".join(map(str, line)).replace("#", ".") for line in mapa]))

mapa = []
f = open("1b.txt")
line = f.readline().strip()

while line != "":
    mapa.append(list(line))
    line = f.readline().strip()


mark = 0
for y in range(len(mapa)):
    for x in range(len(mapa[0])):
        if mapa[y][x] == " ":
            mark += 1
            # print(mark)
            bfs(mapa, (x, y), mark)
            a = 0

# nice_print(mapa)
print(mark)
