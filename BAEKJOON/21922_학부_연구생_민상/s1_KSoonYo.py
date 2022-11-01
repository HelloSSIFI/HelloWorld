import sys
from collections import deque

# pypy3 통과

input = sys.stdin.readline

N, M = map(int, input().split())
labs = [list(map(int, input().split())) for _ in range(N)]
seats = [[False] * M for _ in range(N)]

airs = set()
cnt = 0
for i in range(N):
    for j in range(M):
        if labs[i][j] == 9:
            airs.add((i, j))
            seats[i][j] = True
            cnt += 1

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]       # 상, 하, 좌, 우 : 0, 1, 2, 3

turn_LEFT = {
    0 : 2, 1 : 3, 2 : 1, 3 : 0
}

turn_RIGHT = {
    0 : 3, 1 : 2, 2 : 0, 3 : 1
}


for r, c in airs:
    q = deque([(r, c)])
    while q:
        hr, hc = q.popleft()
        for k in range(4):
            d = dirs[k]
            nr = hr + d[0]
            nc = hc + d[1]

            # 일단 선택한 방향 그대로 진행
            while 0 <= nr < N and 0 <= nc < M:
                if not seats[nr][nc]:
                    seats[nr][nc] = True
                    cnt += 1

                # 에어컨을 만났다면 진행 중지
                if labs[nr][nc] == 9:
                    break

                # 물건 1 : 현재 방향이 왼 or 오일 때, 진행 중지
                # 물건 2 : 현재 방향이 위 or 아래 일 때, 진행 중지
                # 물건 3 : 현재 진행 방향이 왼, 오일때는 왼쪽으로, 위 아래일 때는 오른쪽으로 turn 
                # 물건 4 : 현재 진행 방향이 왼, 오 일때는 오른쪽으로, 위 아래일 때는 왼쪽으로 turn
                if labs[nr][nc] == 1 and (k == 2 or k == 3):
                    break
                elif labs[nr][nc] == 2 and (k == 0 or k == 1):
                    break
                elif labs[nr][nc] == 3:
                    if(k == 0 or k == 1):
                        k = turn_RIGHT[k]
                    elif(k == 2 or k == 3):                    
                        k = turn_LEFT[k]
                elif labs[nr][nc] == 4:
                    if(k == 0 or k == 1):
                        k = turn_LEFT[k]
                    elif(k == 2 or k == 3):                    
                        k = turn_RIGHT[k]
                
                d = dirs[k]
                nr += d[0]
                nc += d[1]

print(cnt)
