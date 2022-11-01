import sys
input = sys.stdin.readline


def pic(obj1, obj2, N, M, x, y):                                # 상하좌우로 총 4번 실행될 함수
    global answer                                               # 입력받은 매개변수에따라 각각 상하좌우에 그림을 걸 수 있는지 확인
    rc = [0, 0]
    for rc[x] in range(N - 1):                                  # 격자의 2칸을 확인하여
        cnt = 0                                                 # 한 칸이 벽이고 나머지 한 칸이 빈 공간일 경우 카운트
        for rc[y] in range(M):                                  # 위와 달라질 경우 현재까지 카운트의 절반을 answer에 더해주고 카운트를 0으로 초기화
            if arr[rc[0]][rc[1]] == obj1 and arr[rc[0] + y][rc[1] + x] == obj2:
                cnt += 1
            else:
                answer += cnt // 2
                cnt = 0


N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]

answer = 0
for obj1, obj2 in [['X', '.'], ['.', 'X']]:                     # 그림의 위치가 빈 공간 기준 위, 아래, 왼쪽, 오른쪽을 각각 탐색
    pic(obj1, obj2, N, M, 0, 1)
    pic(obj1, obj2, M, N, 1, 0)

print(answer)
