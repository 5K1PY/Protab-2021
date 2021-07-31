from Robot2split import split_maze
from Robot2find import find_path

name = "2b"
split_maze(name)

res = 0
for i in range(4):
    res += find_path(f"{name}-{i}.txt")
print(res)
