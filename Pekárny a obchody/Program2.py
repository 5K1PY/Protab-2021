from pulp import *

n = 2

f = open(f"p{n}.txt")
pekarny = list(map(int, f.readline().split()))
f.close()

nejvic = max(pekarny)

f = open(f"o{n}.txt")
obchody = list(map(int, f.readline().split()))
f.close()

f = open(f"c{n}.txt")
ceny = []
for i in range(len(pekarny)):
    ceny.append(list(map(int, f.readline().split())))
f.close()

f = open(f"l{n}.txt")
poplatky = []
for i in range(len(pekarny)):
    poplatky.append(list(map(int, f.readline().split())))
f.close()

model = LpProblem(name="pekarny", sense=LpMinimize)

# proměnné -- x[i][k] podle toho, kolik i-t pekárna veze rohlíků do k-tého obchodu
# proměnná navíc ještě bude chromatické číslo
price = LpVariable(name="price", lowBound=0, cat='Integer')

# počet rohlíků z i-té pekárny do j-tého obchodu
rohliky = []
for i in range(len(pekarny)):
    rohliky.append([])
    for j in range(len(obchody)):
        rohliky[-1].append(LpVariable(name=f"c_{i}_{j}", lowBound=0, cat='Integer'))

dovazky = []
for i in range(len(pekarny)):
    dovazky.append([])
    for j in range(len(obchody)):
        dovazky[-1].append(LpVariable(name=f"l_{i}_{j}", cat='Binary'))


# omezení
## každý pekárna vyveze správný počet rohlíků
for i in range(len(pekarny)):
    model += lpSum(rohliky[i]) == pekarny[i]

## každý obchod dostane správně rohlíků
for j in range(len(obchody)):
    model += lpSum([rohliky[i][j] for i in range(len(pekarny))]) == obchody[j]

# každý zaplatí poplatky
for i in range(len(pekarny)):
    for j in range(len(obchody)):
        model += dovazky[i][j] * nejvic + 0.5 >= rohliky[i][j]

## suma
model += price == lpSum([lpSum([rohliky[i][j]*ceny[i][j] + dovazky[i][j]*poplatky[i][j] for j in range(len(obchody))]) for i in range(len(pekarny))])

# minimalizujeme chromatické číslo
model += price

# řešení (ignorujeme debug zprávy)
status = model.solve(PULP_CBC_CMD(msg=False))
print("výsledek:", int(price.value()))
