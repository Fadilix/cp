import sys

n = int(sys.stdin.readline())
q = n**0.5
s = set()

for i in range(2, int(q + 1)):
    x = i * i

    while x <= n:
        s.add(x)
        x *= i

print(n - len(s))
