from collections import deque
import sys
input = sys.stdin.readline


N, M, T = map(int, input().split())    # 원판의 수, 숫자의 개수, 회전 수

# 원판 데이터
circles = []
for _ in range(N):
    circles.append(deque(map(int, input().split())))

flag = True
for _ in range(T):
    # xi의 배수가 원판 번호, 회전 방향(0: 시계, 1: 반시계, ki: 회전 칸수)
    xi, di, ki = map(int, input().split())

    check = 0    # 원판에 수가 남아있는지 확인
    zeros = 0    # 원판에 0이 있는 개수

    # 회전하기
    for i in range(N):
        check += sum(circles[i])
        zeros += circles[i].count(0)
        if (i+1) % xi == 0:
            if di == 0:
                circles[i].rotate(ki)
            else:
                circles[i].rotate(-ki)

    if check:    # 수가 남아있는 경우 동일한 인접한 수 제거
        delete = set()    # 제거할 인접한 수들의 좌표 저장

        # 같은 원판 내에서 인접한 같은 수 찾기
        for i in range(N):
            for j in range(-1, M-1):
                if circles[i][j]:    # 1 <= 원판에 적힌 수 <= 1000
                    if circles[i][j] == circles[i][j+1]:
                        delete.add((i, j))
                        delete.add((i, j+1))

        # 인접한 원끼리 비교하여 인접한 같은 수 찾기
        for j in range(M):
            for i in range(N-1):
                if circles[i][j]:
                    if circles[i][j] == circles[i+1][j]:
                        delete.add((i, j))
                        delete.add((i+1, j))

        if delete:
            # 인접한 수 제거 (0으로 표기)
            for y, x in delete:
                circles[y][x] = 0
        # 인접하면서 같은 수가 존재하지 않은 경우 원판에 적힌 수의 평균을 구하고, 평균 보다 큰 수에서 1을 빼고 작은 수에서 1을 더한다.
        else:
            avg = check / (N*M-zeros)
            for i in range(N):
                for j in range(M):
                    if circles[i][j]:
                        if circles[i][j] > avg:
                            circles[i][j] -= 1
                        elif circles[i][j] < avg:
                            circles[i][j] += 1

    else:    # 수가 남아 있지 않은 경우 더 이상 확인할 필요가 없다
        flag = False
        break

answer = 0
if flag:
    for i in range(N):
        answer += sum(circles[i])
    print(answer)
else:
    print(0)