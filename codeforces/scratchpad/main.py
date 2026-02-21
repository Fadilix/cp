n = int(input())
s = list(map(int, input().split()))

print(sum([i for i in range(n + 1)]) - sum(s))