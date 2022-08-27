import sys
input = sys.stdin.readline

N = int(input())
arr = [0] + list(map(int, input().split()))                                     # 자신이 팰린드롬일 경우 자신의 양옆에 붙은 수가 같다면
dp = [[1 if i <= j else 0 for i in range(N + 1)] for j in range(N + 1)]         # 그 수도 팰린드롬임을 이용
for i in range(1, N):                                                           # 최초 dp 2차원 배열 중 r >= c 인 부분은 모두 팰린드롬 표시
    for j in range(1, N - i + 1):                                               # 그 후 대각선 방향으로 1과 맞닿아 있는 0 부분을 먼저 탐색하면서
        if dp[1 + j][i + j - 1] == 1 and arr[j] == arr[i + j]:                  # 팰린드롬인지 확인
            dp[j][i + j] = 1

for _ in range(int(input())):
    S, E = map(int, input().split())
    print(dp[S][E])
