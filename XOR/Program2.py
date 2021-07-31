def gen(alpha):
    poz = [0]*len(alpha)
    while poz[0] < len(alpha[0]):
        yield construct(alpha, poz)

        i = len(alpha) - 1
        poz[i] += 1
        while i > 0 and poz[i] >= len(alpha[i]):
            poz[i] = 0
            i -= 1
            poz[i] += 1


def construct(key, poz):
    return [key[i][poz[i]] for i in range(len(key))]


def check(x):
    return (x.isalpha() or x in [".", " ", "?", ",", "-"])


f = open("2.txt", encoding="utf-8")
f.readline()
cisla = list(map(int, f.readline().split(", ")))
f.close()

f = open("res.txt", "w")

x = ord('a')
all_letters = range(x, x+26)

key_lenght = 9
alpha = [[] for i in range(key_lenght)]
for i in range(key_lenght):
    for key in all_letters:
        index = i
        a = True
        while index < len(cisla):
            if not check(chr(key ^ cisla[index])):
                a = False
                break
            index += key_lenght

        if not a:
            continue

        print(f"{i}: {key}")
        alpha[i].append(key)

print(alpha)
for key in gen(alpha):
    print("".join(map(lambda x: chr(x), key)))
    res = []
    for i in range(len(cisla)):
        res.append(cisla[i] ^ key[i % 9])
    text = "".join(map(chr, res))

    print(f"{text}\n")
