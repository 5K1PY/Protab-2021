from itertools import combinations_with_replacement

x = ord("A")
keys = combinations_with_replacement(range(0, 128), 3)

f = open("slova.txt", encoding="utf-8")
slova = []
line = f.readline().strip()
while line != "":
    slova.append(line)
    line = f.readline().strip()
f.close()

f = open("1.txt", encoding="utf-8")
f.readline()
cisla = list(map(int, f.readline().split(", ")))
f.close()

f = open("res.txt", "w")
for key in keys:
    #print(key)
    res = []
    for i in range(len(cisla)):
        res.append(cisla[i] ^ key[i%3])

    # res2 = []
    # for i in range(0, len(cisla)//2):
    #     res2.append(res[i] ^ res[i+97])

    # res3 = []
    # for i in range(0, len(cisla), 2):
    #     res3.append(res[i] ^ res[i+1])

    # res4 = []
    # for i in range(0, len(cisla)//2):
    #     res4.append(res[i] ^ res[-i])

    # for r in (res, res2, res3, res4):
    #     text = "".join(map(chr, r)).lower()
    #     f.write(f"{text}\n")

    #     for slovo in slova:
    #         if slovo in text:
    #             if len(slovo) > 3:
    #                 print(slovo, key)

    text = "".join(map(chr, res))

    a = False
    for char in text:
        if not char.isalpha() and text not in ["/", ".", " ", "?", "!"]:
            a = True
            break
    if a is False:
        f.write(f"{text}\n")

    # for slovo in slova:
    #     if slovo in text:
    #         if len(slovo) > 3:
    #             print(slovo, key)
f.close()
