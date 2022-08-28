"""
시간초과
시간복잡도 : O(n**3)
preSum 만들어서 하니 5% 통과
"""
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    K = int(input())
    cost = list(map(int, input().split()))
    ans = float('inf')
    dp_list = [[-1]*K for _ in range(K)]
    preSum = [0] * (K+1)
    for i in range(1, K+1):
        preSum[i] = preSum[i-1] + cost[i-1]

    def dp(start, end):
        global dp_list
        temp = float('inf')

        if start == end:
            return 0

        if dp_list[start][end] != -1:
            return dp_list[start][end]

        for i in range(start, end):
            temp = min(temp, dp(start, i) + dp(i+1, end) + (preSum[end+1] - preSum[start]))

        dp_list[start][end] = temp
        return temp

    print(dp(0, K-1))