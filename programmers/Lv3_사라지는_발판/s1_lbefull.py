def solution(board, aloc, bloc):
    N = len(board)
    M = len(board[0])
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]


    def dfs(Ar, Ac, Br, Bc, cnt):
        move = []                                                       # 이동 가능한 좌표를 저장할 리스트
        for d in range(4):
            nr = Ar + dr[d]
            nc = Ac + dc[d]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc]:           # 보드 안에 있고 발판이 있다면 move에 추가
                move.append([nr, nc])

        if not board[Ar][Ac] or not move:                               # 현재 턴 캐릭터의 발판이 없거나 움직일 곳이 없으면
            return 1, cnt                                               # 상대가 이겼다는 표시(1)와 현재까지 이동 수를 반환

        board[Ar][Ac] = 0                                               # dfs를 위해 현재 발판을 없애줌
        results = []                                                    # 재귀한 결과값들을 받을 리스트
        for r, c in move:                                               # 이동 가능한 좌표를 돌면서
            results.append(dfs(Br, Bc, r, c, cnt + 1))                  # 재귀 후 결과값을 받아옴

        board[Ar][Ac] = 1                                               # 다시 발판을 만들어 줌
        win = 0                                                         # 재귀 중 한번이라도 이겼는지 판별할 변수
        min_cnt = 100                                                   # 이겼다면 최단거리를 저장
        max_cnt = 0                                                     # 졌다면 최장거리를 저장
        for result in results:                                          # 모든 결과를 확인하면서
            win |= result[0]                                            # 한번이라도 이겼다면 win을 1로 바꿔줌
            if result[0]:                                               # 결과가 이겼으면 min을, 졌다면 max를 갱신
                min_cnt = min(min_cnt, result[1])
            else:
                max_cnt = max(max_cnt, result[1])

        if win:                                                         # 한번이라도 이겼다면
            return 0, min_cnt                                           # 상대가 졌다는 표시(0)와 최단거리를 보내주고
        else:                                                           # 한번도 못이겼다면 반대로 보내줌
            return 1, max_cnt


    answer = dfs(aloc[0], aloc[1], bloc[0], bloc[1], 0)[1]
    return answer


# print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
