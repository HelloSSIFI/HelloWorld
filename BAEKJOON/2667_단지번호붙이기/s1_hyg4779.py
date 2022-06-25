from collections import defaultdict, deque

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

'''
1. 지도 탐색
2. 숫자 & not visit => BFS(현재위치, 단지 번호)
    BFS는 단지 번호 별 집의 개수를 세서 dict에 저장 => defauitdict
3. 지도 내 모든 칸 탐색이 끝나면 return
'''

apart = defaultdict(int)                   # 단지 건물 수 를 저장할 dict
visit = [[0]*N for _ in range(N)]
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]     # 4방향 탐색


def BFS(x, y, number):
    queue = deque([(x, y)])                # 너비우선탐색 큐
    cnt = 0                                # 단지 내 아파트 개수
    while queue:
        ni, nj = queue.popleft()           # 현재 위치
        cnt += 1
        for idx in range(4):
            di, dj = ni + d[idx][0], nj + d[idx][1]     # 4방향 탐색 위치
            if 0 <= di < N and 0 <= dj < N and not visit[di][dj] and arr[di][dj]:
                visit[di][dj] = 1
                queue.append((di, dj))


    apart[number] = cnt


num = 1

for i in range(N):
    for j in range(N):
        if not visit[i][j] and arr[i][j]:
            visit[i][j] = 1
            BFS(i, j, num)                  # 단지 탐색
            num += 1                        # 다음 단지 번호 +1


print(len(apart.values()))
result = sorted(list(apart.values()))

for res in result:
    print(res)