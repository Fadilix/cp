n, w = map(int, input().split())
v = [(tuple(map(int, input().split()))) for _ in range(n)]

v.sort(reverse=True)

res = 0

for val, weight in v:
    take = min(weight, w)
    res += take * val
    w -= take

print(res)