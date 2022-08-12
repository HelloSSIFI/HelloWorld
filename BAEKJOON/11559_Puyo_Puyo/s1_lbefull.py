def gravity():                                                      # 중력 작용
    for c in range(6):
        i = 11                                                      # 각 열을 순회
        while i > -1 and arr[i][c] != '.': i -= 1                   # 맨 아래행부터 빈 공간이 있는 행을 찾음
        for j in range(i, -1, -1):                                  # 빈 공간이 있는 행부터 그 윗줄을 탐색
            if arr[j][c] != '.':                                    # 빈 공간이 아니면
                arr[i][c], arr[j][c] = arr[j][c], arr[i][c]         # 빈 공간이었던 행과 바꿔주고
                i -= 1                                              # 빈 공간 행 인덱스를 한 칸 위로 올려줌


arr = [list(input()) for _ in range(12)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

flag = True
result = 0
while flag:                                                         # 하나라도 뿌요가 터지면 다시 반복
    flag = False                                                    # flag 초기화

    for i in range(12):
        for j in range(6):                                          # 모든 필드 탐색
            if arr[i][j] == '.':                                    # 빈 공간은 건너뜀
                continue

            Q = [(i, j)]
            visited = [[0] * 6 for _ in range(12)]
            visited[i][j] = 1
            k = 0

            while k < len(Q):                                       # 빈 공간이 아니라면
                r, c = Q[k]                                         # BFS 탐색으로 같은 뿌요들을 찾아줌

                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < 12 and 0 <= nc < 6 and not visited[nr][nc] and arr[r][c] == arr[nr][nc]:
                        Q.append((nr, nc))
                        visited[nr][nc] = 1
                k += 1
            
            if len(Q) > 3:                                          # 같은 뿌요가 4개 이상 모였다면
                if not flag:                                        # 현재 반복에서 한번도 뿌요가 터지지 않았다면
                    result += 1                                     # 결과를 +1
                flag = True                                         # falg를 True로 바꿔주고
                for r, c in Q:                                      # 현재 모인 뿌요들을 필드에서 제거
                    arr[r][c] = '.'

    gravity()                                                       # 필드를 다 돌면 중력 작용

print(result)
