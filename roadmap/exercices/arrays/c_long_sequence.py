import sys

n = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
x = int(sys.stdin.readline())

MAX = 10**100
i = 0
# b = lst * MAX

total = sum(lst)
rep = x // total
count = rep * n
s = rep * total

# print(rep, count)

for num in lst:
    s += num
    count += 1

    # print(s)
    if s > x:
        print(count)
        break

# while i < MAX:
#     if s > x:
#         print(i)
#         break
#     s += b[i]
#     i += 1
