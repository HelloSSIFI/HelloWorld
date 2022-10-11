import sys
input = sys.stdin.readline


# idx가 현위치, 해당 값이 이동할 수 있는 칸을 의미
# idx 위치의 점수
board = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17], [18],
         [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]
score_board = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27,
         26, 30, 35, 0]

dice = list(map(int, input().split()))
answer = 0


def search(turn, score, horse):
    global answer

    # 10번 째 턴이 진행이 완료된 경우 종료
    if turn == 10:
        answer = max(answer, score)
        return

    # 4개의 말을 각각 이동하면서 완전탐색
    for i in range(4):

        # 파란색 칸인 경우 파란색 화살표 방향으로 방향 설정
        if len(board[horse[i]]) == 2:
            now = board[horse[i]][1]
        else:
            now = board[horse[i]][0]

        # 주사위 수 만큼 칸 이동(방향 설정에서 이미 한 칸 이동했기 때문에 1칸 적게 이동)
        for _ in range(1, dice[turn]):
            now = board[now][0]

        # 현재 위치가 도착 지점 or 도착지점이 아니지만 좌표에 말이 존재하지 않은 경우 이동이 가능하다.
        if now == 32 or (now < 32 and now not in horse):
            temp = horse[i]
            horse[i] = now
            search(turn + 1, score + score_board[now], horse)
            horse[i] = temp


search(0, 0, [0, 0, 0, 0])

print(answer)