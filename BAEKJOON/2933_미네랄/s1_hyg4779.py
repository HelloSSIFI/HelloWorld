from collections import deque
import sys
input = sys.stdin.readline
R, C = map(int, input().split())

# 동굴
arr = [list(input().rstrip()) for _ in range(R)]
direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]

n = int(input())
# 던진 막대들 높이
stick = list(map(int, input().split()))
for s in range(n):
    stick[s] = R-stick[s]

for turn in range(n):
    # 오른쪽에서 던질 때
    if turn%2:
        for j in range(C-1, -1, -1):
            if arr[stick[turn]][j]=='x':
                arr[stick[turn]][j] = '.'
                break
    # 왼쪽에서 던질 때
    else:
        for j in range(C):
            if arr[stick[turn]][j]=='x':
                arr[stick[turn]][j] = '.'
                break

    # 미네랄 정리
    visit = [[0]*C for _ in range(R)]
    mineral = {True: [], False: []}

    for r in range(R):
        for c in range(C):
            if arr[r][c]=='x' and visit[r][c] == 0:
                Q = deque([(r, c)])
                part = []
                visit[r][c] = 1
                ground = False
                while Q:
                    x, y = Q.popleft()
                    part.append([x, y])
                    for d in direct:
                        nx, ny = x+d[0], y+d[1]
                        if 0 <= nx < R and 0 <= ny < C and visit[nx][ny]==0 and arr[nx][ny]=='x':
                            visit[nx][ny] = 1
                            Q.append((nx, ny))
                            if nx == R-1:ground = True
                if ground:
                    mineral[ground].extend(part)
                else:
                    mineral[ground].append(part)


    new = [['.']*C for _ in range(R)]
    for a, b in mineral[True]:
        new[a][b] = 'x'

    while mineral[False]:
        now = mineral[False].pop(0)
        # 땅 or 땅에붙은 미네랄에 닿을 때까지

        flag = True
        while flag:
            for m in now:
                m[0] += 1

                # 땅에 붙은 수정과 겹치거나 땅에 닿았거나
                if [m[0]+1, m[1]] in mineral[True] or m[0] == R-1:
                    flag = False
        for a, b in now:
            new[a][b] = 'x'
    arr = new


for i in range(R):
    for j in range(C):
        print(arr[i][j], end='')
    print()