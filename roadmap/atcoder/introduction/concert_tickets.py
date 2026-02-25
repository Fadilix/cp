import sys

n, m = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
t = list(map(int, sys.stdin.readline().split()))


ans = []


for c in t:
    h.sort(reverse=True)
    print(h)
    found = False 
    for p in h:
        if p <= c:
            ans.append(p)
            h.remove(p)
            found = True
            break
    if not found:
        ans.append(-1)


print("\n".join(map(str, ans)))

