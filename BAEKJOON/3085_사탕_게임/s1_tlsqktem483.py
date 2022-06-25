import sys

n = int(sys.stdin.readline())
candys = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
d = [(1, 0), (0, 1)]   # 상 우
ans = 0


def search():
    answer = 1

    for i in range(n):
        cnt = 1

        # 열 순회
        for j in range(1, n):
            if candys[i][j] == candys[i][j-1]:
                cnt += 1
            else:
                cnt = 1

            if cnt > answer:
                answer = cnt

        cnt = 1
        # 행 순회
        for j in range(1, n):
            if candys[j][i] == candys[j-1][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt > answer:
                answer = cnt

    return answer


for i in range(n):
    for j in range(n):
        current = candys[i][j]
        for (di, dj) in d:
            next_i = i + di
            next_j = j + dj

            if (next_i < n and next_j < n) and current != candys[next_i][next_j]:
                # 인접 요소 변환
                candys[i][j], candys[next_i][next_j] = candys[next_i][next_j], candys[i][j]
                ans = max(ans, search())

                # 재 변환
                candys[i][j], candys[next_i][next_j] = candys[next_i][next_j], candys[i][j]

print(ans)