import sys
input = sys.stdin.readline


def find_cost():
    global dp
    for r in range(N - 1):
        cost = [2000000] + list(map(int, input().split())) + [2000000]                          # 양 끝지점 인덱스 탐색을 위해 임시로 큰 값을 리스트에 추가
        next_dp = [[2000000] * 3] + [[0] * 3 for _ in range(M)] + [[2000000] * 3]               # dp에 3가지 방향의 비용을 따로 저장
        for c in range(1, M + 1):
            next_dp[c][0] = min(dp[c + 1][1], dp[c + 1][2]) + cost[c]                           # 왼쪽 아래 방향으로 이동하려면 이전 단계의 c+1 인덱스에서 왼쪽 아래(0)을 제외한 1과 2중 작은 값에
            next_dp[c][1] = min(dp[c][0], dp[c][2]) + cost[c]                                   # c로 이동할 비용을 더해준 값이 최소값이 됨
            next_dp[c][2] = min(dp[c - 1][0], dp[c - 1][1]) + cost[c]                           # 나머지 방향도 마찬가지
        dp = next_dp


N, M = map(int, input().split())
dp = [[2000000] * 3] + [[el] * 3 for el in list(map(int, input().split()))] + [[2000000] * 3]
find_cost()

print(min(map(min, dp)))
