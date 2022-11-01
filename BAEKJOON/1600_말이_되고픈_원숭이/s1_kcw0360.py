from collections import deque


K = int(input())
W, H = map(int, input().split())    # W: 가로 , H: 세로
arr = [list(map(int, input().split())) for _ in range(H)]    # 0: 평지, 1: 장애물
visited = [[[-1]*(K+1) for _ in range(W)] for _ in range(H)]

horse = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
monkey = [[-1, 0], [1, 0], [0, -1], [0, 1]]

q = deque()
q.append([0, 0, 0])
visited[0][0][0] = 0
while q:
    a, b, cnt = q.popleft()

    if a == H-1 and b == W-1:
        break

    for d in range(4):
        y = a + monkey[d][0]
        x = b + monkey[d][1]
        # 일반적인 이동
        if 0 <= y < H and 0 <= x < W and arr[y][x] == 0 and visited[y][x][cnt] == -1:
            visited[y][x][cnt] = visited[a][b][cnt] + 1
            q.append([y, x, cnt])

    # 말 이동 방식(횟수가 남아 있을 경우 진행)
    for d in range(8):
        y = a + horse[d][0]
        x = b + horse[d][1]
        if 0 <= y < H and 0 <= x < W and cnt+1 <= K and arr[y][x] == 0 and visited[y][x][cnt+1] == -1:
            visited[y][x][cnt+1] = visited[a][b][cnt] + 1
            q.append([y, x, cnt+1])

answer = 9876543210
for i in range(K+1):
    if -1 != visited[H-1][W-1][i] < answer:
        answer = visited[H-1][W-1][i]

print(answer) if answer != 9876543210 else print(-1)