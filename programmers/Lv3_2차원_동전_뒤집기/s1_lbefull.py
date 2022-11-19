def solution(beginning, target):
    def turn(beginning, target):
        answer = 0
        for c in range(M):                                      # 첫 행의 각 열을 비교하여 다른 부분이 있다면
            if beginning[0][c] == target[0][c]: continue        # 해당 열을 뒤집어줌
            answer += 1
            for r in range(N):
                beginning[r][c] ^= 1

        for r in range(N):                                      # 첫 열의 각 행을 비교하여 다른 부분이 있다면
            if beginning[r][0] == target[r][0]: continue        # 해당 행을 뒤집어줌
            answer += 1
            for c in range(M):
                beginning[r][c] ^= 1
        return answer                                           # 뒤집은 횟수를 리턴


    N = len(beginning)
    M = len(beginning[0])
    copyb = [el[:] for el in beginning]                         # 첫 행을 뒤집고 turn 함수를 실행시키고
    for c in range(M):                                          # 첫 행을 뒤집지 않고 turn 함수를 실행시켜서
        beginning[0][c] ^= 1                                    # 최소값을 찾음

    a1 = turn(copyb, target)
    a2 = turn(beginning, target) + 1                            # 첫 행을 뒤집었으므로 결과 + 1
    answer = min(a1, a2)
    for r in range(N):                                          # target과 다르다면 -1
        if beginning[r] != target[r]: return -1
    return answer


# print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))
