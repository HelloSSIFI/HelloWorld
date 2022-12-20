from collections import deque

def solution(board):
    N = len(board)

    dx, dy = (1, -1, 0, 0), (0, 0, 1, -1)

    # 상하좌우 1칸씩 늘린 board
    field = [[1]*(N+2) for _ in range(N+2)]

    # field board 초기화
    for i in range(N):
        for j in range(N):
            field[i+1][j+1] = board[i][j]

    # BFS
    queue = deque([((1, 1), (1, 2), 0)])
    visit = set()
    visit.add(((1, 1), (1, 2)))

    while queue:
        now1, now2, cnt = queue.popleft()

        # 종점 체크
        if now1 == (N, N) or now2 == (N, N):
            print(cnt)
            return cnt

        # 새로 이동할 수 있는 곳
        sub = set()

        # 평행이동
        for i in range(4):
            nxt1, nxt2 = (now1[0] + dx[i], now1[1] + dy[i]), (now2[0] + dx[i], now2[1] + dy[i])
            if field[nxt1[0]][nxt1[1]] == 0 and field[nxt2[0]][nxt2[1]] == 0:
                sub.add((nxt1, nxt2))

        # 가로 -> 세로
        if now1[0] == now2[0]:
            for j in (-1, 1):
                if field[now1[0]+j][now1[1]] == 0 and field[now2[0]+j][now2[1]] == 0:
                    sub.add((now1, (now1[0]+j, now1[1])))
                    sub.add((now2, (now2[0]+j, now2[1])))

        # 세로 -> 가로로
        if now1[1] == now2[1]:
            for k in (-1, 1):
                if field[now1[0]][now1[1]+k] == 0 and field[now2[0]][now2[1]+k] == 0:
                    sub.add(((now1[0], now1[1]+k), now1))
                    sub.add(((now2[0], now2[1]+k), now2))

        # 방문한 곳 필터링
        for nxt in sub:
            if nxt not in visit:
                visit.add(nxt)
                queue.append((*nxt, cnt+1))

solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]])