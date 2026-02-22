from collections import deque
import sys

n, q = map(int, sys.stdin.readline().split())
s = sys.stdin.readline()

queue = deque(s)

for _ in range(q):
    qry, x = list(map(int, sys.stdin.readline().split()))

    if qry == 1:
        for i in range(x + 1):
            queue.appendleft(queue.pop())

    elif qry == 2:
        print(queue[x - 1])
