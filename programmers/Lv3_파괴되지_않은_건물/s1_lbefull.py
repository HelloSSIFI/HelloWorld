def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    skill_board = [[0] * (M + 1) for _ in range(N + 1)]
    for type, r1, c1, r2, c2, degree in skill:
        sign = 1
        if type == 1:
            sign = -1
        skill_board[r1][c1] += degree * sign                        # 스킬의 시작점과 끝점에 스킬로 건물에 가는 영향을 저장
        skill_board[r1][c2 + 1] += degree * sign * -1               # 문제에서 끝점은 포함되므로 해당 끝점을 표현할 때에는 인덱스 + 1로 표현
        skill_board[r2 + 1][c1] += degree * sign * -1               # 각 스킬이 사각형 모양이므로 4개의 꼭지점을 표현
        skill_board[r2 + 1][c2 + 1] += degree * sign

    restore = 0                                                     # 현재 칸에 스킬로 영향받는 숫자를 저장
    current = [0] * (M + 1)                                         # 매 줄마다 갱신되는 스킬을 저장할 리스트
    for r in range(N):
        for c in range(M + 1):
            current[c] += skill_board[r][c]                         # current에 스킬의 영향을 저장한 후
            restore += current[c]                                   # 현재 칸의 건물에 들어가는 영향을 current에서 가져와서 누적
            if c < M and board[r][c] + restore > 0:                 # 건물이 부서지지 않으면 answer + 1
                answer += 1
    return answer


# print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]], [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
