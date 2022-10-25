def solution(n, s, a, b, fares):
    answer = 300000000
    s -= 1
    a -= 1
    b -= 1
    lines = [[300000000] * n for _ in range(n)]
    for n1, n2, cost in fares:                              # 인접행렬 방식으로 모든 칸을 큰 값으로 초기화
        lines[n1 - 1][n2 - 1] = cost                        # 입력받은 요금대로 인접행렬을 갱신
        lines[n2 - 1][n1 - 1] = cost

    for i in range(n):                                      # 각각의 지점에서 i번을 거쳐서 갈 때의 요금과 비교해 최소값으로 모든 노드 갱신
        for j in range(n):
            for k in range(n):
                if j == k:
                    lines[j][k] = 0
                    continue
                if lines[j][k] > lines[j][i] + lines[i][k]: lines[j][k] = lines[j][i] + lines[i][k]

    for i in range(n):                                      # i번 노드까지 동승하고 그 외에 따로 타는 요금을 계산하여 최소값을 구해줌
        total = lines[s][i] + lines[i][a] + lines[i][b]
        if answer > total: answer = total

    return answer


# print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
