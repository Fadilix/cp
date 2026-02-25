import sys


n, q = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

for i in range(q):
    x, k = map(int, sys.stdin.readline().split())
    count = 0
    found = False
    for i in range(len(arr)):
        if arr[i] == x:
            count += 1
        if count == k:
            print(i + 1)
            found = True
            break
    if not found:
        print(-1)


