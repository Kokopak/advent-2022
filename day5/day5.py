import copy
import re
from collections import deque

stacks_input = True

message = ""
message_p2 = ""

stacks = {}
stacks_p2 = {}

with open("input.txt") as f:

    for row, l in enumerate(f.readlines()):
        if l == "\n":
            stacks_p2 = copy.deepcopy(stacks)
            stacks_input = False

        if stacks_input:
            for col, ch in enumerate(l):
                index_col = col // 4

                if ch.isalpha():
                    stacks[index_col + 1] = stacks.get(index_col + 1, deque())
                    stacks[index_col + 1].appendleft(ch)
        else:
            if l.strip():
                nb_crates, start_pos, end_pos = map(int, re.findall(r"\d+", l))

                new_crates_p2 = deque()

                for i in range(nb_crates):
                    crate = stacks[start_pos].pop()
                    stacks[end_pos].append(crate)

                    crate_p2 = stacks_p2[start_pos].pop()
                    new_crates_p2.appendleft(crate_p2)

                stacks_p2[end_pos].extend(new_crates_p2)

for i in range(1, max(stacks) + 1):
    message += stacks[i][-1]
    message_p2 += stacks_p2[i][-1]

print(message)
print(message_p2)
