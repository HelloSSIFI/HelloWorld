def solution(game_board, table):
    def find_space(target, num):                                    # 격자에서 연속되는 칸의 집합을 찾아 리스트로 만들어 반환하는 함수
        arr = []                                                    # 반환할 리스트
        visited = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if target[i][j] != num or visited[i][j]:
                    continue

                Q = [[i, j]]
                visited[i][j] = 1
                k = 0
                while k < len(Q):                                   # BFS 탐색 후
                    r, c = Q[k]                                     # Q에 모인 좌표들을 arr에 담아줌
                    for d in range(4):                              # 모든 격자 탐색 후 arr 반환
                        nr = r + dr[d]
                        nc = c + dc[d]
                        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and target[nr][nc] == num:
                            Q.append([nr, nc])
                            visited[nr][nc] = 1
                    k += 1
                arr.append(Q)
        return arr


    def hashing(target):                                    # 연속되는 좌표 리스트를 하나의 문자열로 만들어주는 함수
        min_r = 50                                          # 표시하는 위치가 다를 때는 다른 문자열이 되어야 하고
        min_c = 50                                          # 표시하는 위치가 같다면 순서가 달라도 같은 문자열이 되어야 함
        for r, c in target:
            min_r = min(min_r, r)                           # 우선 좌표들 중 r 최소값과 c 최소값을 찾아서
            min_c = min(min_c, c)                           # 모든 좌표값을 최소값으로 빼줘서 블록이 r, c = 0 인곳에 밀착하도록 만들어 줌

        for i in range(len(target)):
            target[i][0] -= min_r
            target[i][1] -= min_c

        target.sort()                                       # 좌표들을 r 우선 c 차선으로 오름차순 정렬
        arr = []                                            # 그 후 각 좌표값들을 문자열로 만들어 순서대로 이어붙임
        for r, c in target:                                 # 칸의 수는 좌표가 6을 넘지 않으므로(한자리 수) 2로 나누어준 값이 칸의 수
            arr.append(str(r))                              # 만들어진 문자열을 반환
            arr.append(str(c))

        return ''.join(arr)


    def rot(target):                                        # 연속되는 좌표리스트를 시게방향으로 회전시키는 함수
        for i in range(len(target)):
            r, c = target[i]
            target[i] = [c, -r]


    N = len(game_board)
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    answer = 0
    
    block = find_space(table, 1)                            # table에서 1이 모여있는 좌표를 찾아 block으로 받아옴
    blank = find_space(game_board, 0)                       # game_board에서 0이 모여있는 좌표를 찾아 blank로 받아옴
    for i in range(len(block)):
        block[i] = hashing(block[i])                        # block의 좌표값들은 모두 hash 문자열로 바꿔줌

    temp = dict()
    for i in block:                                         # hash 문자열 리스트를 딕셔너리로 바꿔서 해쉬와 해쉬의 개수형태로 저장
        temp[i] = temp.get(i, 0) + 1
    block = temp

    for i in range(len(blank)):                             # blank의 좌표들을 순회
        for _ in range(4):                                  # 90도씩 4번 돌릴 수 있으므로 4번 반복
            rot(blank[i])                                   # 시계방향으로 90도 돌려준 뒤
            hashed_blank = hashing(blank[i])                # 해당 좌표를 해쉬로 변환하여
            if block.get(hashed_blank):                     # block 딕셔너리에 있는지 확인
                block[hashed_blank] -= 1                    # 딕셔너리에 있고 그 값이 0보다 크다면
                answer += len(hashed_blank) // 2            # 값을 1 줄여주고 블록의 크기(해쉬값 / 2)를 answer에 추가
                break                                       # 찾았다면 회전은 그만두고 다음 블록을 찾음
    return answer


# print(solution([[0, 0, 0], [1, 1, 0], [1, 1, 1]], [[1, 1, 1], [1, 0, 0], [0, 0, 0]]))
