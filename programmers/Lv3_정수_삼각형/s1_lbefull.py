def solution(triangle):
    for i in range(len(triangle) - 2, -1, -1):              # 삼각형의 아래부터 순회
        for j in range(i + 1):                              # 현재 숫자에 아래방향 두 숫자중 큰 값을 더해줌
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    return triangle[0][0]


# print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
