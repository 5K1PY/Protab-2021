f = open("res")

result = []

line = f.readline().replace(",", "")
while line != "":
    line = line.split()
    result.append((int(line[2]), line[0]))
    line = f.readline().replace(",", "")

print(" ".join(map(lambda x: x[1], sorted(result))))
