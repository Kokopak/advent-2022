from collections import deque

TOTAL = 70000000
NEED = 30000000

path = deque()
fs = {}
listing = False

with open("input.txt") as f:
    for l in f.read().splitlines():
        if l.startswith("$"):
            command = l[2:].split(" ")

            if command[0] == "cd":
                if command[1] != "..":
                    path.append(command[1])
                    fs["/".join(path)] = 0
                else:
                    path.pop()

                listing = False
            else:
                listing = True
                continue

        if listing:
            file_type = l.split(" ")

            if file_type[0].isnumeric():
                tmp_path = path.copy()

                while len(tmp_path) != 0:
                    fs["/".join(tmp_path)] += int(file_type[0])
                    tmp_path.pop()


p1 = 0
p2 = 0

for size in fs.values():
    if size <= 100000:
        p1 += size

for size in sorted(fs.values()):
    if size >= NEED - (TOTAL - fs["/"]):
        p2 = size
        break

print(p1)
print(p2)
