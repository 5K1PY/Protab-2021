f = open("1.txt", encoding="utf-8")
f.readline()
cisla = list(map(int, f.readline().split(", ")))

print(len(cisla))
for i in range(0, len(cisla)//2):
    res = cisla[i] ^ cisla[i+97]
    print(f"{res} {chr(res)}")
