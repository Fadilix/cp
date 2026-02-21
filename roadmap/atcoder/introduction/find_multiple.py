import sys

a, b, c = map(int, sys.stdin.readline().split())

for i in range(a, b + 1):
    if i % c == 0:
        print(i)
        exit(0)

print(-1)