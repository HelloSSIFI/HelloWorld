# pypy3 통과

import sys
input = sys.stdin.readline


def f(p1, p2):
    if p1 == p2:
        return 1
    
    if p1 + 1 == p2:
        if numbers[p1] == numbers[p2]:
            return 1
        else:
            return 0
    
    if dp[p1][p2] != -1:
        return dp[p1][p2]                           # p1 ~ p2 구간을 이미 방문했다면 해당 구간이 팰런드롬인지 아닌지 return

    # 하위 구간으로 가면서 현재 구간을 계속 체크            
    dp[p1][p2] = f(p1 + 1, p2 - 1)                  # 하위 구간이 팰런드롬인지 아닌지에 따라 현재 구간의 팰런드롬도 결정됨

    if dp[p1][p2]:                                  # 하위 구간이 모두 팰런드롬이라면 현재의 구간도 팰런드롬인지 check
        if numbers[p1] != numbers[p2]:
            dp[p1][p2] = 0

    return dp[p1][p2]




N = int(input())
numbers = input().strip().split()
dp = [[-1] * (N) for _ in range(N)]

M = int(input())

result = []
for _ in range(M):
    s, e = map(int, input().split())
    p1 = s - 1                                                  # 구간의 양 끝 단 부터 시작
    p2 = e - 1
    print(f(p1, p2))
        


