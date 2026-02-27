import sys


def get_total(m, k):
    if m <= k:
        return m * (m + 1) // 2

    left = k * (k + 1) // 2
    rows = m - k
    remaining = k - 1 - rows
    right = ((k - 1) * k // 2) - (remaining * (remaining + 1) // 2)

    return left + right

def solve():
    k, x = map(int, sys.stdin.readline().split())

    low, high = 1, 2 * k - 1

    ans = high
    while low <= high:
        mid = (low + high) // 2
        if get_total(mid, k) >= x:
            high = mid - 1
            ans = mid
        else:
            low = mid + 1
    print(ans)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()
