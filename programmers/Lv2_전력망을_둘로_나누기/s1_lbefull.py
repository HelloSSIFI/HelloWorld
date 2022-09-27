from collections import deque


def solution(n, wires):
    answer = n
    lines = [[] for _ in range(n + 1)]
    for v1, v2 in wires:                                # 인접 리스트 형식으로 바꾸어 저장
        lines[v1].append(v2)
        lines[v2].append(v1)

    for v in wires:                                     # 전선 관계를 순회
        dif = [1, 1]                                    # 둘로 나뉜 전력망에 송전탑 개수를 각각 저장
        for i in range(2):                              # 둘로 나뉘었으므로 2번 반복
            Q = deque()
            Q.append(v[i])                              # 현재 전력망 송전탑 번호를 넣고 BFS
            visited = [0] * (n + 1)
            visited[v[i]] = 1

            while Q:
                node = Q.popleft()
                for next_node in lines[node]:
                    if node in v and next_node in v:    # 연결 관계에서 현재 v 연결은 끊겼다고 가정하므로
                        continue                        # v 연결일 경우 건너뜀
                    if not visited[next_node]:
                        visited[next_node] = 1
                        dif[i] += 1
                        Q.append(next_node)

        answer = min(answer, abs(dif[0] - dif[1]))      # 송전탑 개수의 차이를 갱신

    return answer


# print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
