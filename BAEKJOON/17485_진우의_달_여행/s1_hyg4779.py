import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())

MAX = 100*1000

# 연료 사용 첫 줄
dp = [[MAX]*3] + [[el]*3 for el in list(map(int, input().split()))] + [[MAX]*3]

# n-1줄 연료를 받아옴
for i in range(n-1):
    # 다음 연료 사용량 목록
    fuel = [MAX]+list(map(int, input().split()))+[MAX]
    # 이전 연료 사용량 + 현재 연료량을 담을 배열
    # 각 값을 3개씩 나눠놓음 (왼쪽에서 온 값, 수직으로 온 값, 오른쪽에서 온 값
    tmp = [[MAX]*3] + [[0]*3 for _ in range(m)] + [[MAX]*3]

    # tmp 양 끝단을 MAX처리 했으니 가운데부터 탐색. indexerror걱정 없음
    for j in range(1, m+1):
        '''
        왼쪽으로 내려갈 때 사용량
        현 시점에서 오른쪽 상단 위치에서 min(수직으로 내려온 값, 오른편으로 내려온 값) + 현재 연료량
        '''
        tmp[j][0] = min(dp[j + 1][1], dp[j + 1][2]) + fuel[j]
        '''
        수직으로 내려갈 때 사용량
        현 시점에서 수직 상단 위치에서 min(오른쪽으로 내려온 값, 왼쪽으로 내려온 값) + 현재 연료량
        '''
        tmp[j][1] = min(dp[j][0], dp[j][2]) + fuel[j]
        '''
        오른쪽으로 내려갈 때 사용량
        현 시점에서 왼쪽 상단 위치에서 min(왼쪽으로 내려온 값, 수직으로 내려온 값) + 현재 연료량
        '''
        tmp[j][2] = min(dp[j - 1][0], dp[j - 1][1]) + fuel[j]


    # 상단 값 갱신후 반복
    dp = tmp

# 마지막 연료량 중 최솟값 출력
print(min(map(min, dp)))
