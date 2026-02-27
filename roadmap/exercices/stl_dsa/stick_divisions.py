import sys

x, n = map(int, sys.stdin.readline().split())
d = list(map(int, sys.stdin.readline().split()))
d.sort(reverse=True)

count = 0
for e in d:
    if x <= e:
        break
    count += x
    x -= e

print(count)
