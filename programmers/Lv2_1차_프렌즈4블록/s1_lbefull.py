def gravity(m, n, new_board):                           # 중력을 작용시키는 함수
    for c in range(n):
        for r in range(m - 1, -1, -1):                  # 세로줄을 아래부터 보면서
            if not new_board[r][c]:                     # 현재칸이 공간이 있으면
                for i in range(r - 1, -1, -1):          # 위에 제일먼저 발견되는 블럭칸이랑 바꿔줌
                    if new_board[i][c]:
                        new_board[r][c], new_board[i][c] = new_board[i][c], new_board[r][c]
                        break


def solution(m, n, board):
    global new_board
    answer = 0
    new_board = [list(board[i]) for i in range(m)]

    flag = True
    while flag:                                         # 제거할 블럭이 있는동안 반복
        flag = False
        visited = [[0] * n for _ in range(m)]           # 제거할 블록들을 표시
        for r in range(m - 1):                          # 4칸이 제거 가능하면
            for c in range(n - 1):                      # visited에 등록 후 그만큼 정답에 더해줌
                if new_board[r][c] == new_board[r + 1][c] == new_board[r][c + 1] == new_board[r + 1][c + 1] != 0:
                    flag = True
                    for nr, nc in [(r, c), (r + 1, c), (r, c + 1), (r + 1, c + 1)]:
                        if not visited[nr][nc]:
                            answer += 1
                            visited[nr][nc] = 1

        for r in range(m):                              # visited에 등록된 위치에 해당하는
            for c in range(n):                          # 블록들을 0으로 바꿔줌
                if visited[r][c]:
                    new_board[r][c] = 0
        
        gravity(m, n, new_board)                        # 중력 작용

    return answer

# print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
