import sys

tt = int(sys.stdin.readline())

cg = []

while tt:
    q, x = sys.stdin.readline().split()
    x = int(x)
    if q == "a":
        cg.append(x)
    elif q == "t":
        cg.remove(x)
    elif q == "c":
        print(sum(1 for e in cg if e == x))
    tt-= 1
