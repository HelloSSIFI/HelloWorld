from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2**n)]
Q = map(int, input().split())

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for q in Q:
    # 2^1 이상 격자가 생길때만 회전
    if q > 0:
        for i in range(0, 2**n, 2**q):
            for j in range(0, 2**n, 2**q):

                # 작은 격자를 하나 만들어서 회전시키고 값 주입
                tmp = [arr[k][j:j+2**q] for k in range(i, i+2**q)]
                tmp = list(zip(*tmp[::-1]))
                for i2 in range(2**q):
                    for j2 in range(2**q):
                        arr[i+i2][j+j2] = tmp[i2][j2]

    # 녹일 것들
    melt = []
    for r in range(2**n):
        for c in range(2**n):
            cnt = 0

            for d in direct:
                nr, nc = r+d[0], c+d[1]
                if 0 <= nr < 2**n and 0 <= nc < 2**n and arr[nr][nc]:
                    cnt += 1

            # 주변 얼음3개 이하이고 현재위치 얼음있으면 녹일 것 추가
            if cnt < 3 and arr[r][c]:
                melt.append((r, c))

    for r, c in melt:
        arr[r][c] -= 1


# 전체 얼음 양 출력
answer = 0
for line in arr:
    answer += sum(line)
print(answer)


visit = [[0]*(2**n) for _ in range(2**n)]
result = 0

# 가장 큰 덩어리 찾기
for x in range(2**n):
    for y in range(2**n):
        if arr[x][y] and not visit[x][y]:
            cnt = 1
            Q = deque([(x, y)])
            visit[x][y] = 1

            while Q:
                a, b = Q.popleft()
                for d in direct:
                    na, nb = a+d[0], b+d[1]
                    if 0 <= na < 2**n and 0 <= nb < 2**n and visit[na][nb] == 0 and arr[na][nb]:
                        cnt += 1
                        visit[na][nb] = 1
                        Q.append((na, nb))

            # 가장 큰 덩어리 갑 갱신
            result = max(result, cnt)

print(result)