import sys

n = int(sys.stdin.readline())
lst = map(int, sys.stdin.readline().split())

checked = list(range(1, n + 1))
# print(checked)


if len(checked) != len(set(lst)):
    print("No")
    exit(0)

for e in lst:
    if e not in checked:
        print("No")
        exit(0)

print("Yes")
    