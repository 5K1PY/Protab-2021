def cif_sum(x):
    res = 0
    for c in str(x):
        res += int(c)
    return res


f = open("Pi.txt")
pi = "".join(f.readlines()).replace("\n", "").replace(" ", "")

f = open("1.txt")
needed = list(map(int, (f.readline().split())))

for p in needed:
    print(chr(ord("A") + int(pi[p:p+2])-1), end="")
