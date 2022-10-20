import sys
input = sys.stdin.readline


def move(r, c):
    n = shark[(r, c)]
    d = sd[n - 1]
    for nd in pd[n - 1][d]:                                                 # 현재 상어가 바라보는 방향의 우선순위 방향을 순회
        nr = r + dr[nd]                                                     # 새로운 좌표를 구해서
        nc = c + dc[nd]
        if 0 <= nr < N and 0 <= nc < N and smell[nr][nc] < answer:          # 냄새가 없다면 이동
            new_shark[(nr, nc)] = min(new_shark.get((nr, nc), M), n)        # 정보 저장 후 리턴
            sd[n - 1] = nd
            return

    for nd in pd[n - 1][d]:                                                 # 4방향 모두 냄새가 남았다면
        nr = r + dr[nd]
        nc = c + dc[nd]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == n:                # 자신의 냄사가 있는 곳을 찾아서 이동
            new_shark[(nr, nc)] = n                                         # 정보 저장 후 리턴
            sd[n - 1] = nd
            return


N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
sd = list(map(lambda x: int(x) - 1, input().split()))
pd = [[] for _ in range(M)]
for i in range(M):
    for _ in range(4):
        pd[i].append(list(map(lambda x: int(x) - 1, input().split())))

shark = dict()
smell = [[0] * N for _ in range(N)]                     # smell 리스트에는 냄새가 남아있는 시간을 넣어줌
for r in range(N):                                      # arr에는 냄새가 어느 상어인지 번호를 넣어줌
    for c in range(N):
        if arr[r][c]:
            shark[(r, c)] = arr[r][c]                   # shark 딕셔너리에는 key에 좌표를 넣어주고 value에 상어 번호를 넣어줌
            smell[r][c] = K                             # 처음 냄새는 K초까지 지속

answer = 0
while answer < 1000:                                    # 1000초까지 반복
    answer += 1                                         # 시간을 1초 늘려주고
    new_shark = dict()                                  # 상어가 이동한 좌표를 저장할 딕셔너리 선언
    for r, c in shark:                                  # 현재 모든 상어를 움직여줌
        move(r, c)

    if len(new_shark) == 1:                             # 상어가 1마리만 남는다면 반복종료
        break

    shark = new_shark
    for r, c in shark:                                  # 새로운 상어 위치를 모두 탐색
        n = shark[(r, c)]                               # 냄새를 새로 갱신해주고
        smell[r][c] = answer + K                        # 상어 번호 리스트도 갱신
        arr[r][c] = n
else:
    answer = -1                                         # 1000초를 넘는다면 -1

print(answer)
