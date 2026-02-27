import sys

n, m, q = map(int, sys.stdin.readline().split())

stacks = [[] for _ in range(m)]
stacks[0] = [i for i in range(n)]

for _ in range(q):
    c, a, b = sys.stdin.readline().split()
    a, b = int(a), int(b)

    if c == "s":
        stacks[b].append(stacks[a].pop())
    if c == "c":
        if b <= len(stacks[a]):
            print(stacks[a][b])
        else:
            print(-1)


