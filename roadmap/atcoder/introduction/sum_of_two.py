import sys

n, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for idx, e in enumerate(arr):
    trg = x - e
    if trg in arr:
        print(idx + 1, arr.index(trg) + 1)
        exit(0)

print("IMPOSSIBLE")
