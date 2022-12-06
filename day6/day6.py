def get_header(s, n):
    for i in range(len(s)):
        if len(set(s[i:i+n])) == n:
            return i+n

with open("input.txt") as f:
    for l in f.read().splitlines():
        print(get_header(l, 4))
        print(get_header(l, 14))
