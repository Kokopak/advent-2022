from collections import deque

instructions = deque()

with open("input.txt") as f:
    for l in f.read().splitlines():
        inst = l.split(" ")
        instructions.append(inst)


cycles = []
pixel_position = 0
X = 1

inst = instructions.popleft()
next_inst = False

p1 = 0
p2 = ""

nb_cycle = 0

while True:
    if inst[0] == "noop":
        if nb_cycle == 1:
            nb_cycle = 0
            next_inst = True

    elif inst[0] == "addx":
        V = int(inst[1])

        if nb_cycle == 2:
            X += V

            nb_cycle = 0
            next_inst = True

    cycles.append(X)

    if pixel_position in (X - 1, X, X + 1):
        p2 += "#"
    else:
        p2 += "."

    nb_cycle += 1
    pixel_position += 1

    if pixel_position == 40:
        p2 += "\n"
        pixel_position = 0

    if next_inst:
        if len(instructions):
            inst = instructions.popleft()
        else:
            break
        next_inst = False

for i in range(20, 221, 40):
    p1 += cycles[i - 1] * i

print(p1)
print(p2)
