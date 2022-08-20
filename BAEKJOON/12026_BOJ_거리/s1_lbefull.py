N = int(input())
block = input()
dp = [N * N + 1] * N
dp[0] = 0
BOJ = {'B': 'O', 'O': 'J', 'J': 'B'}                        # 다음 밟을 수 있는 블록을 딕셔너리에 표현
for i in range(N - 1):
    if dp[i] == N * N + 1:                                  # 현재 블록이 밟을 수 없는 블록이면 건너뜀
        continue
    for j in range(i, N):
        if BOJ[block[i]] == block[j]:                       # j번 블록이 순서에 맞는 블록이면
            dp[j] = min(dp[j], dp[i] + (j - i) ** 2)        # i번 블록에서 뛸 때와 비교해서 최소값을 갱신

if dp[-1] == N * N + 1:
    dp[-1] = -1
print(dp[-1])
