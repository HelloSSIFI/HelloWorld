import sys
sys.setrecursionlimit(10**9)

parent = [[[i, j] for j in range(51)] for i in range(51)]
graph = [['EMPTY' for _ in range(51)] for _ in range(51)]


def find(y, x):
    if parent[y][x] == [y, x]:
        return parent[y][x]

    parent[y][x] = find(parent[y][x][0], parent[y][x][1])

    return parent[y][x]


def union(a, b, c, d):

    a, b = find(a, b)
    c, d = find(c, d)

    if a == c and b == d:
        return

    if graph[a][b] == 'EMPTY':
        parent[a][b] = [c, d]
    else:
        parent[c][d] = [a, b]


def solution(commands):
    answer = []

    for command in commands:
        command = command.split()

        if command[0] == 'UPDATE':
            if len(command) == 3:    # val1을 val2로 변환
                for i in range(1, 51):
                    for j in range(1, 51):
                        y, x = find(i, j)
                        if graph[y][x] == command[1]:
                            graph[y][x] = command[2]
            else:    # 해당 위치의 셀을 val로 변환
                y, x = find(int(command[1]), int(command[2]))
                graph[y][x] = command[3]

        elif command[0] == 'MERGE':    # 병합
            union(int(command[1]), int(command[2]), int(command[3]), int(command[4]))

        elif command[0] == 'UNMERGE':    # 병합 해제
            y, x = find(int(command[1]), int(command[2]))
            before = graph[y][x]
            temp = []    # 병합 해제하기 위한 좌표 저장

            for i in range(1, 51):    # 병합 해제하기 위한 좌표 찾기
                for j in range(1, 51):
                    if i == command[1] and j == command[2]:
                        continue
                    if [y, x] == find(i, j):
                        temp.append([i, j])

            for a, b in temp:    # 병합 해제
                parent[a][b] = [a, b]
                graph[a][b] = 'EMPTY'

            parent[int(command[1])][int(command[2])] = [int(command[1]), int(command[2])]
            graph[int(command[1])][int(command[2])] = before

        else:    # 프린트
            y, x = find(int(command[1]), int(command[2]))
            answer.append(graph[y][x])

    return answer