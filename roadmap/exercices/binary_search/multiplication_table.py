import sys

def get_count(mid, n):
    count = 1
    for i in range(2, n + 1):
        count += min(n, mid // i)
    return count

def solve():
    n = int(sys.stdin.readline())
    target_count = (n * n) // 2 + 1
    low, high = 1, n * n
    ans = high

    while low <= high:
        mid = (low + high) // 2
        if get_count(mid, n) >= target_count:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)

solve()
