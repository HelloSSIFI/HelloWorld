
def sub_pieces_update(pieces, target_pieces):
    for i in range(len(target_pieces)):
        piece = target_pieces[i]
        pieces[piece][2] = target_pieces[i + 1:]


def forward(moving_pieces, pieces, Play, color, src: tuple, dest: tuple):
    r, c = src
    nr, nc = dest
    target = 0

    # 원래 칸에 있던 기물 정보 갱신
    # 원래 칸에 있는 기물의 길이가 움직이는 기물 길이와 같다면 현재 칸을 0으로 초기화
    bottom_piece = Play[r][c]
    max_len = len(pieces[bottom_piece][2]) + 1 - len(moving_pieces)
    if not max_len:
        Play[r][c] = 0
    else:
        now_pieces = [bottom_piece] + pieces[bottom_piece][2][:max_len - 1]
        for i in range(len(now_pieces)):
            now_p = now_pieces[i]
            pieces[now_p][2] = now_pieces[i + 1:]

    # 다음 칸 바닥 기물 정보 확인
    if not Play[nr][nc]:
        if color == 'w':
            Play[nr][nc] = moving_pieces[0]
        elif color == 'r':
            Play[nr][nc] = moving_pieces[-1]
    else:
        target = Play[nr][nc]

    if color == 'r':
        moving_pieces = moving_pieces[::-1]
    
    for p in range(len(moving_pieces)):
        piece = moving_pieces[p]
        pieces[piece][1] = (nr, nc)

        if not target and piece == Play[nr][nc]:
            continue

        if target:
            pieces[target][2].append(piece)
        elif piece not in pieces[Play[nr][nc]][2]:
            pieces[Play[nr][nc]][2].append(piece)

        # 기물이 4개 이상 쌓이는 순간 게임 종료
        if len(pieces[Play[nr][nc]][2]) >= 3:
            return True

    # 도착 후 기물 별 sub pieces 정보 갱신
    sub_pieces_update(pieces, [Play[nr][nc]] + pieces[Play[nr][nc]][2][:])

def move(N, Map, Play, pieces, colors, dirs, reverse, num):
    piece = pieces[num]
    d = piece[0]
    r, c = piece[1]
    sub_pieces = piece[2][:]

    nr = r + dirs[d][0]
    nc = c + dirs[d][1]
    if 0 < nr <= N and 0 < nc <= N and (colors[Map[nr][nc]] == 'w' or colors[Map[nr][nc]] == 'r'):
        moving_pieces = [num] + sub_pieces
        return forward(moving_pieces, pieces, Play, colors[Map[nr][nc]], (r, c), (nr, nc))
        
    else:
        # 범위 바깥인 경우와 파란색인 경우는 동일
        moving_pieces = [num] + sub_pieces
        d = reverse[d]
        pieces[num][0] = d
        nr, nc = r + dirs[d][0], c + dirs[d][1]
        
        if (0 < nr <= N and 0 < nc <= N) and colors[Map[nr][nc]] != 'b':
            return forward(moving_pieces, pieces, Play, colors[Map[nr][nc]], (r, c), (nr, nc))



N, K = map(int, input().split())
Map = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
pieces = [[] for _ in range(K + 1)]              # i -> 현재 기물 번호, pices[i] -> [방향, 현재 기물 위치, 현재 기물 위로 쌓인 기물 번호 들...]
Play = [[0] * (N + 1)] + [[0] * (N + 1) for _ in range(N)]      # 각 위치에는 가장 바닥에 있는 기물의 번호만 저장

for i in range(1, K + 1):
    r, c, d = map(int, input().split())
    pieces[i].append(d)
    pieces[i].append((r, c))
    pieces[i].append([])
    Play[r][c] = i

colors = {
    0 : 'w', 1 : 'r', 2: 'b'
}

dirs = [0, [0, 1], [0, -1], [-1, 0], [1, 0]]                    # 문제에서 지정한 방향 순서(우, 좌, 상, 하)
reverse = {
    1 : 2, 2: 1, 
    3: 4, 4: 3
}



turn = 1
flag = False

while turn <= 1000:
    for i in range(1, K + 1):
        # 1번부터 K번까지 체스 기물 옮기기
        if move(N, Map, Play, pieces, colors, dirs, reverse, i):
            flag = True
            break
    if flag:
        break
    turn += 1
    
if flag:
    print(turn)
else:
    print(-1)