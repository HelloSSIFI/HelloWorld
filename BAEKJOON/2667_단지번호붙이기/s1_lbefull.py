from collections import deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
result_cnt = 0
result_list = []
Q = deque()

dr = [1, -1, 0, 0]                  # 4방향 탐색
dc = [0, 0, 1, -1]

for i in range(N):                  # 지도 순회
    for j in range(N):
        if not arr[i][j]:           # 집이 없는 곳은 continue
            continue

        result_cnt += 1             # 집이 있으면 단지 + 1
        Q.append((i, j))            # Q에 enQ
        arr[i][j] = 0               # 지도에서 집을 없애줌
    
        cnt = 1                     # 단지 내 집의 개수를 카운트할 변수
        while Q:                    # BFS
            r, c = Q.popleft()

            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]

                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc]:
                    Q.append((nr, nc))
                    cnt += 1
                    arr[nr][nc] = 0
        
        result_list.append(cnt)     # 집 수를 append

result_list.sort()                  # 오름차순 정렬
print(result_cnt)
*map(print, result_list),
