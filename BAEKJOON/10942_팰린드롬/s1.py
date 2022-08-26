import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[0 for _ in range(n)] for _ in range(n)]

for l in range(n):
    for s in range(n-l):
        e = s + l

        # 문자열 1개짜리면 1
        if s == e:
            dp[s][e] = 1

        # 끝문자가 같다면
        elif arr[s] == arr[e]:

            # 2글자 일때
            if s+1 == e:
                dp[s][e] = 1

            # 가운데 문자열이 팰린드롬이면
            elif dp[s+1][e-1] == 1:
                dp[s][e] = 1

for _ in range(int(input())):
    start, end = map(int, input().split())

    print(dp[start-1][end-1])