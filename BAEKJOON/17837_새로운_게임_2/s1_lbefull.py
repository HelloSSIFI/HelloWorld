N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
unit = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(K)]
dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
order = [[[] for i in range(N)] for j in range(N)]                              # 보드에 말이 올라간 순서를 저장할 리스트
for i in range(K):
    r, c, _ = unit[i]
    order[r][c].append(i)                                                       # 초기 말 위치를 order에 올려줌

for cnt in range(1, 1001):                                                      # 최대 1000번 진행
    for i in range(K):                                                          # 말 순서대로 진행
        r, c, d = unit[i]                                                       # 우선 바라보는 방향을 nr, nc로 받아옴
        nr = r + dr[d]
        nc = c + dc[d]

        if (0 > nr or nr >= N or 0 > nc or nc >= N) or board[nr][nc] == 2:      # 파란칸이거나 체스판을 벗어나는 경우
            if d < 2:                                                           # 방향을 반대로 바꿔줌
                d += 1
                d %= 2
            else:
                d += 1
                d %= 2
                d += 2

            unit[i][2] = d                                                      # 바꾼 방향을 저장하고
            nr = r + dr[d]                                                      # 해당 방향칸을 nr, nc로 받음
            nc = c + dc[d]                                                      # 똑같이 파란칸이거나 체스판을 벗어나는 경우는 가만히 두고 다음반복
            if (0 > nr or nr >= N or 0 > nc or nc >= N) or board[nr][nc] == 2:
                continue

        target = []                                                             # 현재 바라보는 방향이 흰 칸이나 빨간칸인경우
        while not target or target[-1] != i:                                    # 현재 말의 위에 올려져있는 말을 모두 target으로 지정
            target.append(order[r][c].pop())                                    # 이 때 순서는 반대가 됨

        if board[nr][nc] == 0:                                                  # 위에서 순서가 반대로 됐으므로 흰 칸일 경우 순서를 바꿔줌
            target = target[::-1]

        for t in target:                                                        # target으로 지정된 말들의 위치 정보를 갱신
            unit[t][0] = nr
            unit[t][1] = nc
        
        order[nr][nc].extend(target)                                            # 이동할 칸에 순서대로 말을 넣어줌

        if len(order[nr][nc]) >= 4:                                             # 만약 이동 후 말이 4개 이상 있으면 종료
            print(cnt)
            exit()

print(-1)
