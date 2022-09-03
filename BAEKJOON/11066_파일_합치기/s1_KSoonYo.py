# pypy3 통과

import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    dp = [[0] * K for _ in range(K)]
    acc = [[0] * K for _ in range(K)]                                           # 최소 누적합을 기록하는 용도
    for i in range(K):
        s, e = 0, i
        while s < K and e < K:
            # 대각선 순으로 채우기(top bottom)
            if s == e:
                dp[s][e] = files[s]
            else:
                minV = float('INF')
                for partition in range(s, e):                                   # 파일을 합칠 수 있는 가능한 모든 경우 탐색
                    a = dp[s][partition] + dp[partition + 1][e]                 # 파일을 합친 결과
                    b = acc[s][partition] + acc[partition + 1][e]               # 현재 파일을 합치기 직전까지의 누적합
                    if a + b < minV:
                        minV = a + b
                        dp[s][e] = a
                        acc[s][e] = a + b                                       # 현재 파일을 합친 결과 누적
            s += 1
            e += 1
    print(acc[0][K - 1])
    