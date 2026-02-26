import sys
import heapq

n = int(sys.stdin.readline())

customers = []
for i in range(n):
    a, d = map(int, sys.stdin.readline().split())
    customers.append((a, d, i))

customers.sort()

# rooms = []
room_assign = [0] * n
heap = []


for a, d, idx in customers:
    if heap and heap[0][0] < a:
        _, room = heapq.heappop(heap)
        room_assign[idx] = room
    else:
        new_idx = len(heap) + 1
        room_assign[idx] = new_idx
        heapq.heappush(heap, (d, new_idx))

print(len(set(room_assign)))
print(*room_assign)

