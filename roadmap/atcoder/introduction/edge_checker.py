import sys

a, b = map(int, sys.stdin.readline().split())

print("YES" if (abs(a - b) == 1 or abs(a - b) == 9) else "NO")