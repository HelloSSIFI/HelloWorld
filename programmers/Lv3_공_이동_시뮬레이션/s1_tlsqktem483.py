"""
풀이 : query 를 거꾸로 돌며 가능한 좌표를 구한다
결과 : 1번제외 시간초과
"""
def solution(n, m, x, y, queries):
    answer = set()
    d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    visited = [[[False for _ in range(len(queries)+1)] for _ in range(m)] for _ in range(n)]

    def move(r, c, qn):
        nonlocal answer

        if qn == -1:
            answer.add((r, c))
            return

        flag = False
        di, distance = queries[qn][0], queries[qn][1]

        if di == 0 and c == 0:
            flag = True
        elif di == 1 and c == m-1:
            flag = True
        elif di == 2 and r == 0:
            flag = True
        elif di == 3 and r == n-1:
            flag = True

        if di in [0, 2]:
            di += 1
        else:
            di -= 1

        # 목표위치가 outline 에 있을 시
        if flag:
            i, j = r, c
            if not visited[i][j][qn]:
                visited[i][j][qn] = True
                move(i, j, qn-1)
            for _ in range(distance):
                if 0 <= i + d[di][0] < n and 0 <= j + d[di][1] < m and not visited[i+d[di][0]][j+d[di][1]][qn]:
                    i += d[di][0]
                    j += d[di][1]
                    visited[i][j][qn] = True
                    move(i, j, qn-1)
                else:
                    break
        # 목표위치가 outline 에 없을 시
        else:
            i, j = r + d[di][0] * distance, c + d[di][1] * distance

            if 0 <= i < n and 0 <= j < m and not visited[i][j][qn]:
                visited[i][j][qn] = True
                move(i, j, qn-1)

    visited[x][y][len(queries)] = True
    move(x, y, len(queries)-1)

    return len(answer)


print(solution(2, 2, 0, 0, 	[[2,1],[0,1],[1,1],[0,1],[2,1]]))
print(solution(2, 5, 0, 1, [[3,1],[2,2],[1,1],[2,3],[0,1],[2,1]]))