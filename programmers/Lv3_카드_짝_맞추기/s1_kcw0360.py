from collections import deque
import copy


answer = 9876543210


def command_move(board, r, c, target_y, target_x):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    q = deque()
    q.append([r, c])
    visited = [[9876543210]*4 for _ in range(4)]    # 커맨드 횟수 체크
    visited[r][c] = 1    # 현재 커서가 선택한 위치(enter +1)

    while q:
        a, b = q.popleft()

        if a == target_y and b == target_x:    # 목표 위치에 도달한 경우 결과 반환
            return visited[a][b]

        for k in range(4):
            y = a + dy[k]
            x = b + dx[k]
            if 0 <= y < 4 and 0 <= x < 4:
                # 한칸 이동 시 현재 위치에서 이동할 때가 더 빠른 경우
                if visited[y][x] > visited[a][b] + 1:
                    visited[y][x] = visited[a][b] + 1
                    q.append([y, x])

                # 카드가 나올때 까지 같은 방향으로 이동 or 카드가 없다면 가장 마지막 칸으로 이동(ctrl키 + 방향키)
                while 4 > y + dy[k] >= 0 == board[y][x] and 0 <= x + dx[k] < 4:
                    y = y + dy[k]
                    x = x + dx[k]

                # ctrl키를 누른 상태에서 이동 했을 때 더 빠른 경우
                if visited[y][x] > visited[a][b] + 1:
                    visited[y][x] = visited[a][b] + 1
                    q.append([y, x])


def dfs(board, r, c, target_y, target_x, cnt):
    global answer
    check = 0    # 카드가 모두 없어졌는지 확인
    target_card = board[target_y][target_x]    # 선택하려는 카드(= 페어가 되는 카드)

    # 타겟이 되는 카드 선택 후 커맨드 횟수 추가
    cnt += command_move(board, r, c, target_y, target_x)
    board[target_y][target_x] = 0    # 카드 없애기

    # 타겟이 되는 카드의 짝의 위치를 찾고은 후 커맨드 횟수 추가
    for i in range(4):
        for j in range(4):
            if board[i][j] == target_card:
                cnt += command_move(board, target_y, target_x, i, j)
                board[i][j] = 0    # 카드 없애기
                r, c = i, j
            check += board[i][j]

    if check:    # 아직 카드가 남아있는 경우
        for i in range(4):
            for j in range(4):
                if board[i][j]:
                    dfs(copy.deepcopy(board), r, c, i, j, cnt)
    else:    # 모든 카드가 없어졌을 때 answer와 cnt 중 적은 값이 answer
        answer = min(answer, cnt)


def solution(board, r, c):
    global answer

    for i in range(4):
        for j in range(4):
            if board[i][j]:
                dfs(copy.deepcopy(board), r, c, i, j, 0)

    return answer