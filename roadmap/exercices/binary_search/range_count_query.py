from collections import defaultdict
from bisect import bisect_left, bisect_right
import sys


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
q = int(sys.stdin.readline())

a.sort()

d = defaultdict(list)
for idx, val in enumerate(a):
    d[val].append(idx)

for _ in range(q):
    l, r, x = map(int, sys.stdin.readline().split())

    if x not in d:
        print(0)
        continue

    left = bisect_left(d[x], l - 1)
    right = bisect_right(d[x], r + 1)

    print(right - left)

