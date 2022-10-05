import copy, sys
input = sys.stdin.readline


N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]


def bfs(temp):
    visited = [[0]*N for _ in range(N)]    # 방문 체크

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # 연합할 국가 시작점 찾기
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:    # 방문 체크 x
                q = [[i, j]]    # q에 좌표 추가
                idx = 0    # 시작 idx
                visited[i][j] = 1    # 방문 체크
                check = [temp[i][j]]    # 현재 국가의 인구수 추가

                while idx < len(q):    # idx가 q의 길이와 같아지면 반복문 종료
                    a, b = q[idx]    # idx에 해당하는 좌표 꺼내기

                    for k in range(4):    # 이동
                        y = a + dy[k]
                        x = b + dx[k]

                        # 범위 안에 존재하고 방문하지 않은 국가인 경우
                        if 0 <= y < N and 0 <= x < N and visited[y][x] == 0:
                            # 인구수 차이가 조건안에 들어오는 경우
                            if L <= abs(temp[a][b] - temp[y][x]) <= R:
                                visited[y][x] = 1    # 방문 체크
                                q.append([y, x])    # 좌표 추가
                                check.append(temp[y][x])    # 인구수 추가
                    idx += 1    # 다음 idx(국가)로 이동

                total = sum(check) // len(check)    # 연합을 이루는 각 칸의 인구수

                for c, d in q:    # 인구수 적용 해주기
                    temp[c][d] = total

    return temp    # 바뀐 인구수 리턴


answer = 0
while True:
    res = bfs(copy.deepcopy(population))    # bfs 결과값

    if population == res:    # 처음 인구수와 변화가 없는 경우
        break
    else:    # 인구수의 변화가 있는 경우
        population = res    # 인구수 덮어쓰기
        answer += 1    # 인구이동 카운트 +1

print(answer)