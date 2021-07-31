from math import lcm

def tick(moons):
    for i in range(len(moons)):
        for j in range(i+1, len(moons)):
            for a in range(3):
                d1, d2 = calc(moons[i].pos[a], moons[j].pos[a])
                moons[i].vel[a] += d1
                moons[j].vel[a] += d2
    for moon in moons:
        for i in range(3):
            moon.pos[i] += moon.vel[i]


def calc(a, b):
    if a < b:
        return (1, -1)
    elif a > b:
        return (-1, 1)
    else:
        return (0, 0)


class Moon():
    def __init__(self, pos):
        self.pos = pos
        self.vel = [0, 0, 0]


moons = [
    Moon([-13, 14, -7]),
    Moon([-18,  9,  0]),
    Moon([0, -3, -3]),
    Moon([-15, 3, -13])
]



saved = [{} for i in range(3)]

res = [0]*3
time = 0
while 0 in res:
    for j in range(3):
        now = tuple([moon.pos[j] for moon in moons] + [moon.vel[j] for moon in moons])
        if res[j] == 0 and now in saved[j]:
            print(res)
            res[j] = time
        else:
            saved[j][now] = time
    if time % 100 == 0:
        print(time)
    tick(moons)
    time += 1

print(lcm(res[0], res[1], res[2]))
print(res)
