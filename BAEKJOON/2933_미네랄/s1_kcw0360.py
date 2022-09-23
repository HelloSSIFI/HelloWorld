from collections import defaultdict, deque


R, C = map(int, input().split())
cave = [list(input()) for _ in range(R)]
N = int(input())
H = list(map(int, input().split()))

def search():
    visited = [[0]*C for _ in range(R)]    # 바닥에 있는 미네랄과 연결되어 있는지 체크
    surface = deque()    # 바닥에 있는 미네랄
    for i in range(C):
        if cave[R-1][i] == 'x':
            surface.append([R-1, i])    # 지면에 있는 미네랄 좌표
            visited[R-1][i] = 1    # 방문 체크

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while surface:    # 바닥에 있는 미네랄과 연결된 미네랄 모두 찾기
        a, b = surface.popleft()

        for k in range(4):
            y = a + dy[k]
            x = b + dx[k]

            if 0 <= y < R and 0 <= x < C and cave[y][x] == 'x' and visited[y][x] == 0:
                visited[y][x] = 1
                surface.append([y, x])

    floating = defaultdict(list)
    for i in range(R-1, -1, -1):
        for j in range(C):
            if cave[i][j] == 'x' and visited[i][j] == 0:    # 떠있는 클러스터
                floating[j].append(i)

    if floating:    # 떠있는 클러스터가 있는 경우
        interval = 100    # 떨어져야할 높이
        for j in floating.keys():    # 떨어져야 하는 높이 구하기
            for i in floating[j]:
                for y in range(i+1, R):
                    if cave[y][j] == 'x' and y not in floating[j]:
                        interval = min(interval, y-i-1)
                    if y == R-1 and cave[y][j] == '.':
                        interval = min(interval, y-i)

        for key in floating.keys():    # 떨어뜨리기
            for val in floating[key]:
                cave[val][key] = '.'
                cave[val+interval][key] = 'x'


for idx in range(len(H)):
    h = R - H[idx]
    if idx % 2 == 0:    # 왼쪽에서 막대기 투척
        for c in range(C):
            if cave[h][c] == 'x':
                cave[h][c] = '.'
                search()
                break
    else:    # 오른쪽에서 막대기 투척
        for c in range(C-1, -1, -1):
            if cave[h][c] == 'x':
                cave[h][c] = '.'
                search()
                break


ans = []
for i in range(R):
    temp = ''
    for j in range(C):
        temp += cave[i][j]
    temp += '\n'
    ans.append(temp)

print(''.join(ans))