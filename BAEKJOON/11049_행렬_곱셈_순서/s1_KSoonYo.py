# pypy3 통과

import sys
input = sys.stdin.readline

n = int(input())
mats = []
dp = [[[(0, 0), 2 ** 31] for _ in range(n)] for _ in range(n)]            # 인덱스: n - 1번째 행렬, 값: [행렬곱 결과(row, col), 개수]
'''
dp 형태(A: 5x3, B: 3x2, C: 2x6)
        A(0)         B(1)             C(2)
A(0)    A            AxB            AxBxC -> min(A(BC), (AB)C)
    (5, 3), 0 |  (5, 2), 30 |

                     B             BxC
B(1)          |  (3, 2), 0  |     (3, 6), 36

                                    C
C(2)                        |     (2, 6), 0

'''

for _ in range(n):
    r, c = map(int, input().split())
    mats.append((r, c))

for i in range(n):
    # 대각선 순으로 dp 채우기
    s, e = 0, i                     # 시작점 항상 0, 끝점은 i를 따라감
    partition = e - 1               # 분할 기준은 끝점 e보다 1 작음

    while s < n and e < n:
        if s == e:
            # 행렬 1개인 경우
            # 행렬곱 연산 횟수는 0
            dp[s][e][0] = mats[s]
            dp[s][e][1] = 0
        else:
            # 1) 행렬곱 연산결과 저장
            # 행렬곱의 연산결과는 dp 상 현재 위치에서 (s, partition) 행렬의 첫번째 인자와 (partition + 1, e)의 두번째 인자로 이루어짐
            # 즉 dp의 현재 위치에서 왼쪽에 있는 행렬곱 연산결과의 0번째, 아래쪽에 있는 행렬곱 연산결과의 1번째 인자를 취함  
            dp[s][e][0] = (dp[s][partition][0][0], dp[partition + 1][e][0][1])

            # 2) 행렬곱 연산횟수 저장
            # 시작점에서 partition 까지(즉 현재 위치에서 한 칸 왼쪽 column index, 한 칸 아래쪽 row index에 있는 행렬 위치까지)
            # 행렬곱 연산횟수 최소값 갱신
            for j in range(s, partition + 1):
                dp[s][e][1] = min(dp[s][e][1], dp[s][j][1] + dp[j + 1][e][1] + (dp[s][j][0][0] * dp[j + 1][e][0][0] * dp[j + 1][e][0][1]))
        s += 1
        e += 1
        partition = e - 1

print(dp[0][n-1][1])

