from collections import defaultdict
import sys
input = sys.stdin.readline


N, K = map(int, input().split())
board_color = [list(map(int, input().split())) for _ in range(N)]    # 색깔 확인 보드 (0: 흰색, 1: 빨강, 2: 파랑)
chessboard = [[[] for _ in range(N)] for _ in range(N)]    # 체스 말 표기
chess = defaultdict(list)    # 말 위치 저장
for k in range(1, K+1):
    a, b, d = map(int, input().split())
    chess[k] = [a-1, b-1, d-1]
    chessboard[a-1][b-1].append(k)

# 방향
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
turn_dir = {0: 1, 1: 0, 2: 3, 3: 2}

def game():
    answer = 1
    flag = 0    # 방향 전환 체크
    while answer < 1000:    # 1000 보다 큰 경우 조건문 빠져나가기
        for idx in range(1, K+1):
            a, b, d = chess[idx]
            y = a + dy[d]
            x = b + dx[d]

            # 체스판을 벗어나거나 이동하는 칸이 파란색인 경우 방향 전환
            if y < 0 or N <= y or x < 0 or N <= x or board_color[y][x] == 2:
                cd = turn_dir[d]    # 방향 전환
                y = a + dy[cd]    # 바뀐 방향의 이동 좌표
                x = b + dx[cd]

                # 제자리에 있는 경우 방향만 바꿔준다
                if y < 0 or N <= y or x < 0 or N <= x or board_color[y][x] == 2:
                    chess[idx][2] = cd    # 바뀐 방향 저장
                    continue
                flag = 1    # 방향 전환 체크

            # 이동하는 칸이 흰색인 경우
            if board_color[y][x] == 0:
                line = chessboard[a][b].index(idx)    # 현재 말의 번호가 현재 위치의 말들 중 어느 위치에 있는지 확인
                move = chessboard[a][b][line:]    # 현재 말부터 아래에 쌓인 말들
                chessboard[a][b] = chessboard[a][b][:line]    # 현 위치는 현재 말의 하단에 있는 말만 새로 저장
                chessboard[y][x].extend(move)    # 이동 하는 곳에 현재 말부터 상단의 말까지 순서대로 저장

                if len(chessboard[y][x]) >= 4:    # 말이 4개 쌓아지는 경우
                    return answer

                for i in move:    # 함께 이동한 말들은 변경된 위치 저장
                    chess[i][0], chess[i][1] = y, x

                if flag == 1:    # 방향이 바뀐 말들은 바뀐 방향 저장
                    chess[idx][2] = cd
                    flag = 0

            # 이동하는 칸이 빨간색인 경우
            elif board_color[y][x] == 1:
                line = chessboard[a][b].index(idx)
                move = chessboard[a][b][line:]
                chessboard[a][b] = chessboard[a][b][:line]
                move.reverse()    # 쌓는 순서 반대로 뒤집기
                chessboard[y][x].extend(move)

                if len(chessboard[y][x]) >= 4:    # 말이 4개 쌓아지는 경우
                    return answer

                for i in move:
                    chess[i][0], chess[i][1] = y, x

                if flag == 1:
                    chess[idx][2] = cd
                    flag = 0

        answer += 1

    return -1

print(game())