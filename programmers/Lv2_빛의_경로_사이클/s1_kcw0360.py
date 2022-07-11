def solution(grid):
    global answer, visited
    w, h = len(grid[0]), len(grid)
    answer = []
    # 가로 세로 방향으로 방문체크 하기 위한 visited
    visited = [[[0] * 4 for _ in range(w)] for _ in range(h)]

    direction = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}

    # 모든 경우의 수 확인
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for d in range(4):
                if visited[i][j][d]:
                    continue

                cnt = 0    # 지가나는 격자 카운트
                dy, dx = i, j
                while visited[dy][dx][d] == 0:
                    visited[dy][dx][d] = 1    # 현재 경로 체크
                    cnt += 1    # 지나간 격자 세기

                    # 방향 전환
                    if grid[dy][dx] == 'R':
                        d = (d + 5) % 4
                    elif grid[dy][dx] == 'L':
                        d = (d + 7) % 4

                    # 이동경로가 idx 이내의 범위인지 확인
                    dy = (dy + direction[d][0]) % h
                    dx = (dx + direction[d][1]) % w

                answer.append(cnt)    # while문을 빠져나왔다면 더 이상 새경로를 탐색할 수 없기 때문에 while문에서 이동한 경로 정보 추가

    # 조건대로 결과값을 오름차순 정렬하여 return
    return sorted(answer)