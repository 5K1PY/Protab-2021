from math import sqrt


def backtrack(l):
    global pocet
    global dilky
    global pouzite

    # print(len(l))

    if len(l) == pocet ** 2:
        resolve(l)

    for d in dilky:
        for i in range(8):
            d.next()
            if d.num in pouzite:
                continue

            if len(l) % pocet == 0:
                if len(l) >= pocet:
                    if d.top != l[len(l) - pocet].bottom:
                        continue

            else:
                if d.left != l[-1].right:
                    continue
                if len(l) >= pocet:
                    if d.top != l[len(l) - pocet].bottom:
                        continue

            l.append(d)
            pouzite.add(d.num)
            backtrack(l)
            pouzite.remove(d.num)
            l.pop()


def resolve(l):
    global res
    res += 1
    print(res)

class Dilek:
    def __init__(self, num, border):
        self.num = num

        self.top = border[0]
        self.bottom = border[-1]
        self.left = "".join([l[0] for l in border])
        self.right = "".join([l[-1] for l in border])

        self.counter = 0

    def __repr__(self):
        return self.num

    def __str__(self):
        return self.num

    def turn(self):
        self.right, self.bottom, self.left, self.top = self.top, self.right[::-1], self.bottom, self.left[::-1]

    def flip(self):
        self.top, self.right, self.bottom, self.left = self.top[::-1], self.left, self.bottom[::-1], self.right

    def next(self):
        if self.counter == 3:
            self.flip()
        else:
            self.turn()
        self.counter = (self.counter + 1) % 4


f = open("2b.txt")

pouzite = set()
dilky = []

res = 0
line = f.readline().strip()
while line != "":
    number = int(line.split()[1])
    f.readline().strip()

    border = []
    line = f.readline().strip()
    while line != "":
        border.append(line)  
        line = f.readline().strip()

    dilky.append(Dilek(number, border))
    line = f.readline().strip()

pocet = int(sqrt(len(dilky)))
backtrack([])
print(res / 8)
