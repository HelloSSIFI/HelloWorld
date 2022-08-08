# pypy3 통과

import sys
input = sys.stdin.readline

maximum = int(input())
passengers = list(map(int, input().split()))                                    # 각 객차 별 승객 수(인덱스: 객차, 값: 승객 수)
sub_maximum = int(input())
dp = [[0] * (len(passengers) + 1) for _ in range(4)]                            # i번째 소형기관차가 N번 객차 범위 이내로 실을 수 있는 최대 승객 수 기록
total = [0] + [sum(passengers[:i]) for i in range(1, len(passengers) + 1)]      # N번째 객차까지의 승객 수 합



for i in range(1, 4):
    for j in range(sub_maximum, len(passengers) + 1):
        # 점화식: 1번째 ~ 3번째 소형기관차 중 i번째 기관차가 바로 이전 객차 범위(j - 1)까지 실은 최대 승객 수 
        # vs 
        # i-1번째 소형기관차(이전 소형기관차)가 j - sub_maximum 범위까지 실은 최대 승객 수 + 현재 소형 기관차가 새로 실을 j - sub_maximum ~ j번째 까지의 총 승객 수 
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - sub_maximum] + (total[j] - total[j - sub_maximum]))

print(dp[3][maximum])
