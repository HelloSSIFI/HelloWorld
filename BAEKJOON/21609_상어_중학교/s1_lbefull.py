def bfs(i, j, color):                               # BFS 탐색
    Q = [[i, j]]                                    # Q의 좌표들은 블록을 제거하는데 사용될 수 있으므로
    used = [[0] * N for _ in range(N)]              # deque대신 list를 사용
    used[i][j] = 1
    rainbow = idx = 0
    while idx < len(Q):                             # idx가 Q보다 작은동안 반복
        r, c = Q[idx]
        idx += 1
        for d in range(4):                          # 4방향 탐색
            nr = r + dr[d]                          # 조건에 맞는 블록을 Q에 담아주고
            nc = c + dc[d]                          # 무지개 블록의 개수를 카운트
            if 0 <= nr < N and 0 <= nc < N and (arr[nr][nc] == 0 or arr[nr][nc] == color) and not used[nr][nc]:
                used[nr][nc] = 1
                Q.append([nr, nc])
                if arr[nr][nc] == 0:
                    rainbow += 1

    return Q, rainbow                               # Q와 무지개 블록 개수를 리턴


def remove_block(blocks):                           # 넘겨받은 좌표들을 빈칸(-2)으로 만들어 주는 함수
    for r, c in blocks:
        arr[r][c] = -2


def gravity():                                                  # 중력 작용 함수
    for c in range(N):                                          # 모든 열 탐색
        er = br = N - 1                                         # 행은 맨 아래 행부터 탐색
        while True:                                             # er은 빈칸의 행번호, br은 블록인 칸의 행번호 탐색
            flag = False
            while er >= 0 and arr[er][c] > -2: er -= 1          # 범위 내에서 빈 칸의 행번호를 er에 저장
            while br >= 0 and arr[br][c] < 0:                   # 블록의 행 번호를 찾음
                if arr[br][c] == -1:                            # 만약 검은 블록을 만나면
                    br -= 1                                     # er과 br 모두 검은 블록위로 위치시킨 후
                    er = br                                     # 다시 처음부터 반복
                    flag = True
                    break
                br -= 1                                         # 검은 블록이 아닐경우 행을 위로 탐색하며 블록인 칸을 찾음

            if flag:                                            # 위의 br을 찾는 동안 검은 블록을 만난경우 다음반복
                continue

            if er < 0 or br < 0:                                # 둘 중 하나라도 좌표범위를 벗어나면 반복종료
                break

            if br > er:                                         # 블록이 더 아래에 있다면
                br = er                                         # 좌표를 빈칸으로 설정하고 빈칸의 위를 다시 탐색
                continue

            arr[er][c], arr[br][c] = arr[br][c], arr[er][c]     # 빈 칸과 블록 칸을 바꿔줌


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
answer = 0
while True:                                                     # 조건에 맞는 동안 반복
    visited = [[0] * N for _ in range(N)]
    max_rainbow = -1
    max_Q = []
    for r in range(N):
        for c in range(N):                                      # 행과 열을 순차적으로 탐색
            if arr[r][c] <= 0 or visited[r][c]:                 # 일반 블록이 아니거나 이미 탐색한 블록은 다음반복
                continue

            Q, rainbow = bfs(r, c, arr[r][c])                   # 일반블록일 경우 BFS 탐색 후 Q와 무지개 블록 개수를 받아옴
            for i, j in Q:                                      # 받은 좌표들을 순회
                if arr[i][j] != 0:                              # 무지개 블록이 아닌 좌표들을
                    visited[i][j] = 1                           # visited에 표시

            if len(Q) < 2:                                      # 블록 그룹이 2개 미만이면 다음반복
                continue

            if len(max_Q) < len(Q) or (len(max_Q) == len(Q) and max_rainbow <= rainbow):
                max_rainbow = rainbow                           # 문제의 조건 우선순위에 맞다면
                max_Q = Q                                       # 해당 그룹을 변수에 저장

    if not max_Q:                                               # 2개 이상의 그룹이 없다면
        break                                                   # 반복 종료

    answer += len(max_Q) ** 2                                   # 블록 개수의 제곱만큼 점수를 더해줌
    remove_block(max_Q)                                         # 블록 제거
    gravity()                                                   # 중력 작용
    arr = list(map(list, zip(*arr)))[::-1]                      # 반시계방향 90도 회전
    gravity()                                                   # 중력 작용

print(answer)
