from collections import deque

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(places):
    answer = []

    for place in places:                                    # 대기실 별로 순회
        good = True
        for i in range(5):
            isRuled = True                                  
            for j in range(5):
                temp = True
                if place[i][j] == 'P':                      # P: 대기자의 위치 탐색
                    temp = BFS(place, (i,j))                # 대기자 반경으로 맨헤튼 거리 이내 탐색
                if not temp:                                # 거리두기가 지켜지지 않고 있다면
                    isRuled = False                         # 해당 순회 중단
                    break

            if not isRuled:                                 # 도중에 순회가 중단되었다면
                answer.append(0)                            # 거리두기가 안지켜진 것이므로 배열에 0 추가
                good = False
                break
        if good:                                            # 거리두기가 모두 지켜졌다면
            answer.append(1)                                # 배열에 1 추가
                               
    return answer

def BFS(place, start):
    q = deque([start])                                      # start: 첫 출발 위치 좌표
    visited = [[0] * 5 for _ in range(5)]
    while q:
        point = q.popleft()

        if point != start and place[point[0]][point[1]] == 'P':
            return False

        for dir in range(4):
            nx = point[0] + dx[dir]
            ny = point[1] + dy[dir]
            
            if 0 <= nx < 5 and 0 <= ny < 5 and (nx, ny) != start:
                ndist_x = max((start[0] - nx), -(start[0] - nx)) 
                ndist_y = max((start[1] - ny), -(start[1] - ny)) 

                ndist = ndist_x + ndist_y
                if ndist <= 2 and not visited[nx][ny] and place[nx][ny] != 'X':
                    visited[nx][ny] = ndist
                    q.append((nx, ny))

    return True

print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
