from collections import deque

N, K = map(int, input().split())

q = deque()
q.append(N)

cnt = 0
check = [-1] * 100001
check[N] = 0

while q:
    now = q.popleft()

    if now == K:cnt += 1

    for y in [now * 2, now + 1, now - 1]:
        if 0 <= y < 100001:
            if check[y] == -1 or check[y] >= check[now]+1: # 시간: 방문한 적 없거나 현재시간 +1인경우
                check[y] = check[now]+1                    # 시간 최신화
                q.append(y)                                # 갈수 있는 경우의 수 추가

print(check[K])
print(cnt)