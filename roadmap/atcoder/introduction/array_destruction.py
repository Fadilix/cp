import sys
from typing import Counter

def solve():
    n = int(sys.stdin.readline())
    n = 2 * n
    a = list(map(int, sys.stdin.readline().split()))
    a.sort(reverse=True)

    c = Counter(a)

    for i in range(n):
        x = a[0] + a[i]
        res = check(x, a[:], n, c.copy())
        if res:
            print("YES")
            print(x)
            for o, p in res:
                print(o, p)
            return

    print("NO")

def check(x, a, n, c):
    ops = []

    for i in range(n):
        val = a[i]
        if c[val] == 0:
            continue

        target = x - val
        c[val] -= 1

        if c[target] > 0:
            c[target] -= 1
            ops.append((val, target))
            x = val
        else:
            return None
    return ops


tt = int(sys.stdin.readline())
for _ in range(tt):
    solve()
