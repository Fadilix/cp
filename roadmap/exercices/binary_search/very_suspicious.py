import sys
from bisect import bisect_left

def solve():
    max_n = 1000005
    v = [0] * max_n

    v[0] = 0
    v[1] = 0
    v[2] = 2

    current_add = 2
    for i in range(3, max_n):
        if i % 3 != 0:
            current_add += 2

        v[i] = v[i-1] + current_add

    t = int(sys.stdin.readline())
    results = []

    for _ in range(t):
        n = int(sys.stdin.readline())
        ans = bisect_left(v, n)
        results.append(str(ans))

    print("\n".join(results))

solve()
