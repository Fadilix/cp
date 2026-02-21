def binomial_coefficient(n, k):
    if n < k:
        return 0
    if n == 0 or k == 0:
        return 1
        
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = 1
    
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][k]



def naive(matrix, y, x):
    def max_path(i, j):
        if i == 0 and j == 0:
            return matrix[0][0]
        if i == 0:
            return matrix[0][j] + max_path(0, j - 1)
        if j == 0:
            return matrix[i][0] + max_path(i - 1, 0)
        return matrix[i][j] + max(max_path(i - 1, j), max_path(i, j - 1))
    return max_path(y - 1, x - 1)


print(naive([[5, 3, 2, 1],
             [1, 2, 10, 1],
             [4, 3, 2, 20],
             [2, 1, 1, 1]], 4, 4))
print(naive([[-92]], 1, 1))


import queue

q = queue.PriorityQueue()
q.put((1, 'task1'))
q.put((3, 'task3'))
q.put((2, 'task2'))