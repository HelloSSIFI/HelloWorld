def rotation(m, q):
    min_v = 10001
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우 하 좌 상
    temp = []
    for i in range(len(m)):
        temp_list = []
        for j in range(len(m[i])):
            temp_list.append(m[i][j])
        temp.append(temp_list)
    y_1, x_1, y_2, x_2 = q[0]-1, q[1]-1, q[2]-1, q[3]-1

    d_idx = 0
    i, j = y_1, x_1
    for _ in range((x_2-x_1)*2 + (y_2-y_1)*2):
        if min_v > m[i][j]:
            min_v = m[i][j]
        (di, dj) = d[d_idx]
        next_i, next_j = i + di, j + dj
        temp[next_i][next_j] = m[i][j]

        if (next_i in [y_1, y_2]) and (next_j in [x_1, x_2]):
            d_idx += 1
        i, j = next_i, next_j
    return temp, min_v


def solution(r, c, queries):
    ans = []
    n_map = [[0]*c for _ in range(r)]
    n = 1
    for i in range(r):
        for j in range(c):
            n_map[i][j] = n
            n += 1

    for query in queries:
        temp, min_v = rotation(n_map, query)
        n_map = temp
        ans.append(min_v)

    return ans


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
print(solution(3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))