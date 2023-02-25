from collections import deque


def find(island, sy, sx, w, d):
    cnt = int(island[sy][sx])    # 출발지점
    q = deque([(sy, sx)])
    island[sy][sx] = 'X'    # 방문 체크

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        a, b = q.popleft()

        for k in range(4):
            y = a + dy[k]
            x = b + dx[k]

            if 0 <= y < d and 0 <= x < w and island[y][x].isdigit():    # 연결된 땅인지 확인
                cnt += int(island[y][x])    # 머물수 있는 날짜 더하기
                island[y][x] = 'X'    # 방문 체크
                q.append((y, x))    # 다음 땅을 찾기 위해 좌표를 q에 추가

    return island, cnt


def solution(maps):
    answer = []
    w, d = len(maps[0]), len(maps)

    for i in range(d):    # 문자열을 리스트로 변경
        maps[i] = list(maps[i])

    for i in range(d):
        for j in range(w):
            if maps[i][j].isdigit():    # 바다가 아닌 경우 연결된 땅 탐색
                maps, day = find(maps, i, j, w, d)
                answer.append(day)    # answer에 머물 수 있는 날짜 추가

    # 무인도가 존재한다면 [-1], 아니면 정렬해서 return
    if answer:
        answer.sort()
        return answer
    else:
        return [-1]