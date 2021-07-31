from string import ascii_uppercase

"""Fills dead ends in maze."""

mapa = []
f = open("2b.txt")
line = f.readline().strip()
starts = []

while line != "":
    mapa.append(list(line))
    line = f.readline().strip()

f.close()

changed = True
while changed:
    changed = False
    for sy in range(1, len(mapa)-1):
        for sx in range(1, len(mapa[0])-1):
            if mapa[sy][sx] != " " and mapa[sy][sx] not in ascii_uppercase:
                continue

            pocet = 0
            dx, dy = 1, 0

            for i in range(4):
                x, y = sx + dx, sy + dy
                if mapa[y][x] == "#":
                    pocet += 1
                dx, dy = -dy, dx

            if pocet >= 3:
                mapa[sy][sx] = "#"
                changed = True

f = open("2f.txt", "w")
for line in mapa:
    f.write(f"{''.join(line)}\n")
f.close()
