import sys

def check(limit, k, arr):
    s = 0
    count = 1

    for x in arr:
        if x > limit:
            return False
        if s + x > limit:
            count += 1
            s = x
        else:
            s += x

    return count <= k


def solve():
    _, k = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))

    lo, hi = max(arr), sum(arr)

    ans = hi
    while lo <= hi:
        mid = (lo + hi) // 2
        if check(mid, k, arr):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1
    print(ans)

solve()

