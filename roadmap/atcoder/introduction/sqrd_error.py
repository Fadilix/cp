import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

result = 0
for i in range(len(a)):
    for j in range (i + 1, len(a)):
        result += (a[i] - a[j]) ** 2

print(result)