from itertools import permutations
from collections import deque


def solution(board, r, c):
    def bfs(sr, sc, num):                                                               # sr, sc에서 가장 조작을 적게하여 num이 쓰여진 카드를 찾아
        visited = [[0] * 4 for _ in range(4)]                                           # 조작횟수와 위치를 반환
        visited[sr][sc] = 1
        Q = deque()
        Q.append((sr, sc))
        while Q:                                                                        # sr, sc로부터 bfs 시작
            cr, cc = Q.popleft()
            if copy_board[cr][cc] == num:                                               # num위치일 경우
                copy_board[cr][cc] = 0                                                  # 해당 위치를 0으로 바꿔주고 횟수와 좌표반환
                return visited[cr][cc] - 1, cr, cc

            for d in range(4):
                nr = cr + dr[d]
                nc = cc + dc[d]
                if 0 <= nr < 4 and 0 <= nc < 4:                                         # bfs 탐색
                    if not visited[nr][nc]:                                             # 인접한 상하좌우 일 경우 방문한 적이 없다면 Q에 넣어주고 조작횟수를 기록
                        visited[nr][nc] = visited[cr][cc] + 1
                        Q.append((nr, nc))
                    while 0 <= nr < 4 and 0 <= nc < 4 and copy_board[nr][nc] == 0:      # 인접한 위치가 빈 공간(0)일 경우, 카드가 나올 때까지 이동
                        nr = nr + dr[d]
                        nc = nc + dc[d]
                    if nr < 0 or 4 <= nr or nc < 0 or 4 <= nc:                          # 만약 인덱스 범위를 벗어났다면 다시 한칸 뒤로
                        nr = nr - dr[d]
                        nc = nc - dc[d]
                    if not visited[nr][nc]:                                             # 카드가 있는곳이 방문한 적이 없는곳이면
                        visited[nr][nc] = visited[cr][cc] + 1                           # 조작횟수를 기록하고 Q에 넣어줌
                        Q.append((nr, nc))
        return -1, -1, -1


    answer = 10000000
    N = 0
    for i in range(4):
        if N < max(board[i]): N = max(board[i])                     # 카드짝의 개수를 N으로 저장
    order = list(range(1, N + 1))
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    for p in permutations(order, N):                                # 카드를 찾는 순서의 모든 경우(순열)를 찾음
        move = 0                                                    # 순열마다 이동 횟수를 저장할 변수
        copy_board = [el[:] for el in board]                        # 보드를 변경하므로 원본을 카피해서 사용
        sr = r                                                      # 시작점을 sr, sc 로 받아옴
        sc = c
        for n in p:                                                 # 순열대로 카드를 찾기 시작
            cnt, nr, nc = bfs(sr, sc, n)                            # 시작점에서 bfs를 이용해 현재 찾고있는 n번 카드 중 조작 횟수가 더 적은 카드를 찾아서 위치와 횟수를 받음
            move += cnt + 1                                         # 조작 횟수에 enter를 입력하는 경우 1을 더해서 추가해줌
            cnt, nr, nc = bfs(nr, nc, n)                            # 받아온 위치에서 다른 n번 카드가 있는곳을 bfs 탐색
            move += cnt + 1                                         # 마찬가지로 이동 + enter 횟수를 추가해줌
            sr = nr                                                 # 마지막 위치를 sr, sc로 설정하고 다음 번호 카드를 찾음
            sc = nc
        if answer > move: answer = move
    return answer


# print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
