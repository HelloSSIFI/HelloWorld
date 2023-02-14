from collections import deque


def solution(x, y, n):
    visited = [-1] * 1000001
    visited[x] = 0
    Q = deque([x])
    while Q:                                                    # 숫자 x를 Q에 넣고 BFS
        z = Q.popleft()
        if z + n <= 1000000 and visited[z + n] == -1:           # n을 더하고 해당 수를 아직 체크하지 않았으면
            visited[z + n] = visited[z] + 1                     # 현재 연산수 +1로 체크하고 Q에 넣어줌
            Q.append(z + n)

        for i in range(2, 4):                                   # 2와 3을 각각 곱하고 해당 수를 체크하지 않았다면
            if z * i <= 1000000 and visited[z * i] == -1:       # 현재 연산수 +1로 체크하고 Q에 넣어줌
                visited[z * i] = visited[z] + 1
                Q.append(z * i)

    return visited[y]


# print(solution(10, 40, 5))
