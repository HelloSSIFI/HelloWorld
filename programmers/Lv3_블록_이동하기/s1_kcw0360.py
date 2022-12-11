from collections import deque


def solution(arr):
    n = len(arr)
    board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            board[i+1][j+1] = arr[i][j]

    q = deque([((1, 1), (1, 2), 0)])    # 시작점 추가
    check = {((1, 1), (1, 2))}  # 드론이 지나간 자리 체크
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        now1, now2, cnt = q.popleft()

        # 최종 위치에 도달한 경우
        if now1 == (n, n) or now2 == (n, n):
            return cnt

        # 이동이 가능한 다음 경로 찾기
        temp = []
        for k in range(4):
            nxt1, nxt2 = (now1[0] + dy[k], now1[1] + dx[k]), (now2[0] + dy[k], now2[1] + dx[k])
            if board[nxt1[0]][nxt1[1]] == 0 and board[nxt2[0]][nxt2[1]] == 0:
                temp.append((nxt1, nxt2))

        # 로봇 회전 하기
        rot = [-1, 1]
        if now1[0] == now2[0]:  # 가로
            for r in rot:
                if board[now1[0] + r][now1[1]] == 0 and board[now2[0] + r][now2[1]] == 0:
                    temp.append((now1, (now1[0] + r, now1[1])))
                    temp.append((now2, (now2[0] + r, now2[1])))

        else:  # 세로
            for r in rot:
                if board[now1[0]][now1[1] + r] == 0 and board[now2[0]][now2[1] + r] == 0:
                    temp.append(((now1[0], now1[1] + r), now1))
                    temp.append(((now2[0], now2[1] + r), now2))

        # 다음 이동 위치가 지나온 위치가 아닌 경우 q와 check에 추가
        for nxt in temp:
            if nxt not in check:
                q.append((*nxt, cnt + 1))
                check.add(nxt)
