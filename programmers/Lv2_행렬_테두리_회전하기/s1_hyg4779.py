def solution(rows, columns, queries):
    ans = []
    arr = [[(columns*row)+(col+1) for col in range(columns)] for row in range(rows)]

    direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 시계 방향

    for x1, y1, x2, y2 in queries:
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        min_v = float('INF')                  # 탐색할 배열에 가장 작은 수
        idx = 0
        nr, nc = x1, y1
        pre = arr[nr][nc]

        while idx < 4:
            if pre < min_v:min_v = pre        # 최소값 갱신
            sr, sc = nr + direct[idx][0], nc + direct[idx][1]

            if x1 <= sr <= x2 and y1 <= sc <= y2:
                tmp = arr[sr][sc]
                arr[sr][sc] = pre
                pre = tmp

                nr, nc = sr, sc
            else:
                idx += 1
        ans.append(min_v)

    return ans

print(*solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]))