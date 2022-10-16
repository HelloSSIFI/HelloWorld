import sys
input = sys.stdin.readline


N, M, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
direction = list(map(int, input().split()))
smell = [[[0, 0]]*N for _ in range(N)]    # [냄새의 상어 번호, 냄새 남은 시간]

priorities = [[] for _ in range(M)]    # 상어의 회전 방향 우선 순위
for i in range(M):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = 0
while True:
    # 냄새 정보 업데이트
    for i in range(N):
        for j in range(N):
            # 냄새가 존재하는 경우, 시간 1초 감소
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1

            # 상어가 존재하는 경우 냄새 표시
            if arr[i][j]:
                smell[i][j] = [arr[i][j], K]

    # 상어 이동
    temp = [[0]*N for _ in range(N)]    # 임시 결과 저장용
    for i in range(N):
        for j in range(N):
            if arr[i][j]:    # 상어 위치한 곳
                d = direction[arr[i][j]-1]    # 현재 상어의 방향
                check = False
                # 냄새가 안나는 곳 찾기
                for idx in range(4):
                    y = i + dy[priorities[arr[i][j]-1][d-1][idx]-1]
                    x = j + dx[priorities[arr[i][j]-1][d-1][idx]-1]
                    if 0 <= y < N and 0 <= x < N:
                        if smell[y][x][1] == 0:    # 냄새가 존재하는 곳
                            # 이미 상어가 있다면 번호가 낮은 상어가 자리 차지
                            # 상어 방향 변경
                            direction[arr[i][j]-1] = priorities[arr[i][j]-1][d-1][idx]
                            # 상어 이동
                            if temp[y][x] == 0:
                                temp[y][x] = arr[i][j]
                            else:
                                temp[y][x] = min(temp[y][x], arr[i][j])
                            check = True
                            break

                if check:
                    continue

                # 주변에 냄새가 모두 남아 있는 경우 자신의 냄새가 있는 곳으로 이동
                for idx in range(4):
                    y = i + dy[priorities[arr[i][j]-1][d-1][idx]-1]
                    x = j + dx[priorities[arr[i][j]-1][d-1][idx]-1]
                    if 0 <= y < N and 0 <= x < N:
                        if smell[y][x][0] == arr[i][j]:    # 자신의 냄새가 있는 곳
                            direction[arr[i][j]-1] = priorities[arr[i][j]-1][d-1][idx]
                            temp[y][x] = arr[i][j]
                            break

    arr = temp    # 상어 위치 최신화
    answer += 1    # 시간 +1

    # 1번 상어만 남았는지 체크
    flag = True
    for i in range(N):
        for j in range(N):
            if arr[i][j] > 1:
                flag = False

    if flag:    # 1번 상어만 남은 경우 정답 출력
        print(answer)
        break

    if answer >= 1000:    # 1000초까지 답이 1번 상어만 남지 않았다면 -1 출력
        print(-1)
        break