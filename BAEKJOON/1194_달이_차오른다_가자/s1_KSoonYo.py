import sys
from collections import deque

input = sys.stdin.readline


N, M = map(int, input().split())
Map = [input().strip() for _ in range(N)]

checked = [[[False] * (2 ** 6 + 1) for _ in range(M)] for _ in range(N)]               # 현재 아무런 열쇠를 지니고 있지 않은 상태 표시 [r][c][열쇠 상태 체크]

# 비트마스킹
# value 값만큼 비트를 << 연산자로 이동
key_table = {
    'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4, 'f' : 5
}

# 시작점 찾기
start = tuple()
for r in range(N):
    for c in range(M):
        if Map[r][c] == '0':
            start = (r, c)
            checked[r][c][0] = True
            break
    if start:
        break

# 0은 현재 아무런 열쇠도 가지고 있지 않은 상태
q = deque([[start, 0, 0]])                   # [출발점, 열쇠 상태, 거리]
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

while q:
    s = q.popleft()

    r, c = s[0]
    key = s[1]
    dist = s[2]

    if Map[r][c] == '1':
        print(dist)
        exit()

    for d in dirs:
        nr = r + d[0]
        nc = c + d[1]
        # 방문이 가능한 경우
        if 0 <= nr < N and 0 <= nc < M and Map[nr][nc] != '#'  and not checked[nr][nc][key]:

            # 다음 칸이 열쇠 칸일 때, 내가 가지고 있지 않는 거라면 열쇠 상태 갱신 후 진입
            if 'a' <= Map[nr][nc] <= 'z':
                temp_key = key | (1 << key_table[Map[nr][nc]])
                checked[nr][nc][temp_key] = True
                q.append([(nr, nc), temp_key, dist + 1])

            # 다음 칸이 문 칸일 때, 내가 맞는 키를 가지고 있는 상태라면 진입
            elif 'A' <= Map[nr][nc] <= 'Z':
                if key & (1 << key_table[Map[nr][nc].lower()]):
                    checked[nr][nc][key] = True
                    q.append([(nr, nc), key, dist + 1])

            else:
                checked[nr][nc][key] = True
                q.append([(nr, nc), key, dist + 1])        
            
            
print(-1)