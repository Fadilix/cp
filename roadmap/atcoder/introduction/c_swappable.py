import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

count = 0

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if 1 <= i < j <= n + 1 and lst[i - 1] != lst[j - 1]:
            count += 1

print(count)
