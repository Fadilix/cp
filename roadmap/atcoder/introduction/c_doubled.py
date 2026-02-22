import sys


n = int(sys.stdin.readline())
count = 0

for i in range(1, n + 1):
    s = str(i)
    if len(s) % 2 != 0:
        continue

    mid = len(s) // 2

    first = s[:mid]
    second = s[mid:]
    if first == second:
        count += 1

print(count)