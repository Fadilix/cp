import sys

q = int(sys.stdin.readline())

A = []
while q:
    query = list(map(int, sys.stdin.readline().split()))

    c = query[0]
    if c == 1:
        _, x  = query
        A.append(x)
    elif c == 2:
        _, x, k = query
        lex = [i for i in A if i <= x]
        dance = 0
        found = False
        lex.sort(reverse=True)

        for i in lex:
            if k > 5:
                break
            if dance == k - 1:
                found = True
                print(i)
                break
            # a.remove(i)
            dance += 1
        if not found:
            print(-1)

    elif c == 3:
        _, x, k = query
        gex = [i for i in A if i >= x]
        dance = 0
        found = False
        gex.sort()

        for i in gex:
            if k > 5:
                break
            if dance == k - 1:
                found = True
                print(i)
                break
            # A.remove(i)
            dance += 1
        if not found:
            print(-1)

    q -= 1

