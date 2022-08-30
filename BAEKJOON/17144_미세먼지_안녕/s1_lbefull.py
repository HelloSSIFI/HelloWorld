import sys
input = sys.stdin.readline


def air_work(i, d):                         # 공기청정기 작동
    temp = A[i][1]
    A[i][1] = 0
    for c in range(2, C):                   # 한줄씩 인덱스에 맞춰 옮겨줌
        temp2 = A[i][c]
        A[i][c] = temp
        temp = temp2

    r = i + d
    while 0 <= r < R:
        temp2 = A[r][C - 1]
        A[r][C - 1] = temp
        temp = temp2
        r += d
    
    r -= d
    for c in range(C - 2, -1, -1):
        temp2 = A[r][c]
        A[r][c] = temp
        temp = temp2
    
    r -= d
    while r < i or r > i:
        temp2 = A[r][0]
        A[r][0] = temp
        temp = temp2
        r -= d


R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
q = []
air = []
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for r in range(R):                              # 공기 청정기의 r 좌표를 air에 넣어줌
    if A[r][0] == -1:
        air.append(r)

while T > 0:                                    # 시간만큼 반복
    for r in range(R):
        for c in range(C):                      # 최초 미세먼지 위치를 q에 넣어줌
            if A[r][c] > 0:
                q.append((r, c, A[r][c]))
    
    while q:                                    # q에있는 미세먼지를 조건에 맞게 확산
        r, c, dust = q.pop()
        new_dust = dust // 5
        for d in range(4):                      # 4방향을 확인
            nr = r + dr[d]                      # 인덱스 범위 내에 있고
            nc = c + dc[d]                      # 공기청정기가 아니면 원래위치에서 새로운 위치로 먼지 확산
        
            if 0 <= nr < R and 0 <= nc < C and A[nr][nc] != -1:
                A[r][c] -= new_dust
                A[nr][nc] += new_dust
    air_work(air[0], -1)                        # 공기 청정기 작동
    air_work(air[1], 1)                         # 위 아래 나누어서 작동
    T -= 1

answer = 2
for r in range(R):
    answer += sum(A[r])
print(answer)
