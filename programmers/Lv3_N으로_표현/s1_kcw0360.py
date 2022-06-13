def solution(N, number):

    if N == number:
        return 1

    dp = [[] for i in range(9)]

    for i in range(1, 9):
        dp[i].append(int(str(N)*i))

        for j in range(1, i):
            for x in dp[j]:
                for y in dp[i-j]:
                    dp[i].append(x+y)
                    dp[i].append(x-y)
                    dp[i].append(x*y)
                    if y != 0:
                        dp[i].append(x//y)

        if number in dp[i]:
            return i

    return -1