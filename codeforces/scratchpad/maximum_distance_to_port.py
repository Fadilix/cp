from collections import defaultdict, deque

n, m, k = map(int, input().split())
a = list(map(int, input().split()))

G = defaultdict(list)

for i in range(m):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

Q = deque([1])
dist = [-1] * (n + 1)
dist[1] = 0

while Q:
    node = Q.popleft()
    for nei in G[node]:
        if dist[nei] == -1:
            dist[nei] = dist[node] + 1
            Q.append(nei)

result = [0] * (k + 1)


for city in G:
    ptype = a[city -1]
    result[ptype] = max(result[ptype], dist[city])

print(result[1:])
