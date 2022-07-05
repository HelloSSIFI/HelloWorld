from collections import deque


def solution(places):
    def bfs(r, c, arr):

        visit = [[0] * 5 for _ in range(5)]
        visit[r][c] = True
        queue = deque([(r, c, 0)])

        while queue:
            ni, nj, dist = queue.popleft()
            for d in direct:
                si, sj = ni + d[0], nj + d[1]
                if 0 <= si < 5 and 0 <= sj < 5 and not visit[si][sj]:

                    if arr[si][sj] == 'O':  # 빈자리면 추가 & 파티션이면 갈 수 없음
                        visit[si][sj] = True
                        queue.append((si, sj, dist+1))

                    elif arr[si][sj] == 'P':  # 사람을 만나면 return False
                        if dist+1 <= 2:
                            return False

        return True


    direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    ans = [1, 1, 1, 1, 1]

    for now in range(5):
        array = places[now]

        i, j = 0, 0
        while i < 5:

            if array[i][j] == 'P':
                if not bfs(i, j, array):
                    ans[now] = 0
                    break

            j += 1
            if j == 5:
                i += 1
                j = 0

    return ans
