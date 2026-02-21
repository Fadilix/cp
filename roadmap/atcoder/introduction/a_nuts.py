import sys

n = sys.stdin.readline()
lst = map(int, sys.stdin.readline().split())

count = 0
for nuts in lst:
    if nuts > 10:
        count += nuts - 10
print(count)