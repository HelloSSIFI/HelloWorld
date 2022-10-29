import sys
input = sys.stdin.readline


N, M = map(int, input().split())    # N: 세로, M: 가로
arr = [list(input()) for _ in range(N)]
check = [[[0]*M for _ in range(N)] for _ in range(4)]    # 그림 걸기 [0: 좌, 1: 우, 2: 상, 3: 하]
answer = 0

for y in range(1, N-1):
    for x in range(1, M-1):
        if arr[y][x] == '.':    # 현 위치가 빈 공간인 경우
            if arr[y+1][x] == ".":    # 현 위치의 윗칸도 빈 공간인 경우
                if arr[y][x-1] == "X" and arr[y+1][x-1] == "X" and check[0][y][x] == 0:    # 빈 공간 좌측이 벽이면서 그림이 안걸려있다면
                    check[0][y][x] = 1    # 그림 걸기
                    check[0][y+1][x] = 1    # 그림 걸기
                    answer += 1    # 그림 개수 추가
                if arr[y][x + 1] == "X" and arr[y+1][x+1] == "X" and check[1][y][x] == 0:
                    check[1][y][x] = 1
                    check[1][y+1][x] = 1
                    answer += 1
            if arr[y][x+1] == ".":    # 현 위치의 우측도 빈 공간인 경우
                if arr[y-1][x] == "X" and arr[y-1][x+1] == "X" and check[2][y][x] == 0:
                    check[2][y][x] = 1
                    check[2][y][x+1] = 1
                    answer += 1
                if arr[y+1][x] == "X" and arr[y+1][x+1] == "X" and check[3][y][x] == 0:
                    check[3][y][x] = 1
                    check[3][y][x+1] = 1
                    answer += 1

print(answer)