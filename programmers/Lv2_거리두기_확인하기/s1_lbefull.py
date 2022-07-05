from collections import deque

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def solution(places):
    answer = []
    for place in places:                                    # 각각의 대기실 순회
        examinees = []                                      # 응시자 위치를 저장할 리스트
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':                      # 응시자 위치를 추가
                    examinees.append((i, j))
        
        for examinee in examinees:                          # 각각의 응시자위치를 순회
            Q = deque()
            Q.append(examinee)                              # Q에 enQ 후 방문표시
            visited = [[0] * 5 for _ in range(5)]
            visited[examinee[0]][examinee[1]] = 1

            flag = False
            while Q:                                        # BFS
                r, c = Q.popleft()

                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]

                    if 0 <= nr < 5 and 0 <= nc < 5 and not visited[nr][nc]:
                        if place[nr][nc] == 'P':
                            answer.append(0)                # 만약 거리두기 실패면
                            flag = True                     # 결과에 0 추가 후
                            break                           # 현재 응시자순회까지 반복이 빠져나가도록 flag 설정

                        if place[nr][nc] == 'O' and visited[r][c] + 1 < 3:
                            visited[nr][nc] = visited[r][c] + 1
                            Q.append((nr, nc))              # 2칸 거리까지만 탐색
                
                if flag:
                    break
            if flag:
                break
        else:
            answer.append(1)                                # 거리두기 성공이면 결과에 1 추가

    return answer
