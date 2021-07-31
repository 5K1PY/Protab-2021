from itertools import combinations_with_replacement


def check(x):
    return (x.isalpha() or x in [".", " ", "?", ",", "-"])


f = open("1.txt", encoding="utf-8")
f.readline()
cisla = list(map(int, f.readline().split(", ")))
f.close()

f = open("res.txt", "w")

x = ord('a')
all_letters = range(x, x+26)

key_lenght = 3
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

for a1 in alpha[0]:
    for a2 in alpha[1]:
        for a3 in alpha[2]:
            key = [a1, a2, a3]
            print("".join(map(lambda x: chr(x), key)))
            res = []
            for i in range(len(cisla)):
                res.append(cisla[i] ^ key[i % 3])
            text = "".join(map(chr, res))

            print(f"{text}\n")
