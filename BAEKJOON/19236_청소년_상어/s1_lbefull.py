import copy


def dfs(sum_eat, sr, sc, sd, arr_copy):
    global answer
    arr = copy.deepcopy(arr_copy)                                                   # 공간을 복사
    for i in range(1, 17):                                                          # 물고기를 오름차순으로 이동
        flag = True
        for r in range(4):
            for c in range(4):
                if not arr[r][c] or arr[r][c][0] != i:                              # 현재 칸이 비었거나 이동할 물고기가 아니라면 다음반복
                    continue

                cnt = 0
                while flag:                                                         # 8방향 탐색
                    nr = r + dr[arr[r][c][1]]
                    nc = c + dc[arr[r][c][1]]

                    if 0 <= nr < 4 and 0 <= nc < 4 and [nr, nc] != [sr, sc]:        # 인덱스 범위 내에 있고 상어 위치가 아니라면
                        flag = False                                                # 해당 위치로 이동하면서 자리를 바꿔주고 다음 번호의 물고기 탐색
                        arr[r][c], arr[nr][nc] = arr[nr][nc], arr[r][c]
                    else:                                                           # 해당 칸으로 못간다면
                        cnt += 1                                                    # 방향을 바꿔서 다시시도
                        arr[r][c][1] = (arr[r][c][1] + 1) % 8                       # 8방향 모두 안된다면 다음 물고기 탐색
                        if cnt == 8: flag = False

                if not flag:
                    break
            if not flag:
                break

    target = []                                                                     # 상어가 먹을 수 있는 물고기 좌표 리스트
    for k in range(4):
        nr = sr + dr[sd] * k
        nc = sc + dc[sd] * k
        if 0 <= nr < 4 and 0 <= nc < 4 and arr[nr][nc]:                             # 바라보는 방향에 물고기를 모두 넣어줌
            target.append((nr, nc))

    if target:                                                                      # 먹을 수 있는 물고기가 하나라도 있다면
        for nr, nc in target:                                                       # 해당 위치로 이동하면서
            temp = arr[nr][nc][:]                                                   # 물고기를 먹어주고
            arr[nr][nc] = []                                                        # 재귀 후 다시 물고기 원상복구
            dfs(sum_eat + temp[0], nr, nc, temp[1], arr)
            arr[nr][nc] = temp[:]
    else:                                                                           # 먹을 수 있는 물고기가 하나도 없다면
        if sum_eat > answer: answer = sum_eat                                       # 결과 갱신


arr = [[] for _ in range(4)]
for i in range(4):
    info = list(map(int, input().split()))
    for j in range(0, 8, 2):
        arr[i].append([info[j], info[j + 1] - 1])

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

sd = arr[0][0][1]
answer = arr[0][0][0]
arr[0][0] = []

dfs(answer, 0, 0, sd, arr)

print(answer)
