def solution(queue1, queue2):

    n, m = sum(queue1), sum(queue2)

    l = len(queue1)
    answer = l

    dp = [[[0, 0] for _ in range(l*2)] for _ in range(l*2)]
    dp[0][0] = [n, m]


    def dfs(a, b):
        nonlocal answer
        if dp[a][b][0] == dp[a][b][1]:
            answer = min(answer, a+b)
            return a+b

        if a+1 < l*2:
            if a//l:
                dp[a+1][b] = [dp[a][b][0]-queue2[a%l], dp[a][b][1]+queue2[a%l]]
            else:
                dp[a+1][b] = [dp[a][b][0]-queue1[a%l], dp[a][b][1]+queue1[a%l]]
            dfs(a+1, b)

        if b+1 < l*2:
            if b//l:
                dp[a][b+1] = [dp[a][b][0]+queue1[b%l], dp[a][b][1]-queue1[b%l]]
            else:
                dp[a][b+1] = [dp[a][b][0]+queue2[b%l], dp[a][b][1]-queue2[b%l]]
            dfs(a, b+1)

    dfs(0, 0)

    return -1 if answer == l else answer


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))