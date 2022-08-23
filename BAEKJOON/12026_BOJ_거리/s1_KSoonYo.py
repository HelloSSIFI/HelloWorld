import sys
input = sys.stdin.readline

N = int(input())
blocks_group = input().strip()
dp = [float('inf')] * N
step_table = {                                              # step 순서 table 정의
    'B' : 'O',                                              # ex) B 다음에는 O를 밟아야 한다.
    'O' : 'J',
    'J' : 'B'
}

# dp[n] 정의 : n번째 블록까지 오는 데 필요한 에너지 양(k*k)

dp[0] = 0                                                   # 첫 step은 0
for i in range(N):
    step = blocks_group[i]                                  # 현재 step
    for j in range(i + 1, N):                               # 현재 스탭 이후에 있는 보도블록 탐색
        if blocks_group[j] == step_table[step]:             # j번째에 다음에 밟을 보도블록이 나오면
            dp[j] = min(dp[j], dp[i] + (j - i) ** 2)        # J번째에 이미 기록된 값 vs 현재 블록에서 j번째 블록까지 갈 때 필요한 에너지 합 중 최소값 갱신

if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])