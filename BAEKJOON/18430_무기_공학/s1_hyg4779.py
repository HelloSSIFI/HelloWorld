# 부메랑 종류
V = [
    [(0, -1), (1, 0)],
    [(-1, 0), (0, -1)],
    [(-1, 0), (0, 1)],
    [(0, 1), (1, 0)]
]

n, m = map(int, input().split())
wood = [list(map(int, input().split())) for _ in range(n)]

if n == 1 or m == 1:
    print(0)
    exit()

visit = [[0] * m for _m in range(n)]
answer = 0


# 중심제외 부분 인덱스 return
def rest(r, c, k) -> tuple:
    r1, c1 = r + V[k][0][0], c + V[k][0][1]
    r2, c2 = r + V[k][1][0], c + V[k][1][1]
    return r1, c1, r2, c2


# 부메랑이 만들어 질 수 있는지 판별
def check(r, c, k):
    r1, c1, r2, c2 = rest(r, c, k)
    if (((0 <= r1 < n and 0 <= r2 < n) and (0 <= c1 < m and 0 <= c2 < m))
            and (visit[r1][c1] == 0 and visit[r2][c2] == 0)):
        return True
    else:
        return False


# 중심부분*2 해서 강도 return
def score(r, c, k):
    r1, c1, r2, c2 = rest(r, c, k)
    return wood[r][c] * 2 + wood[r1][c1] + wood[r2][c2]


# 완전탐색
def dfs(i, j, now):
    global answer

    if now > answer:
        answer = now

    for r in range(i, n):
        for c in range(j, m):
            if visit[r][c]:
                continue

            for k in range(4):
                if check(r, c, k):

                    r1, c1, r2, c2 = rest(r, c, k)
                    visit[r][c], visit[r1][c1], visit[r2][c2] = 1, 1, 1

                    # now에 점수 더하고 다음 인덱스 부터 탐색
                    dfs(r, c+1, now+score(r, c, k))
                    visit[r][c], visit[r1][c1], visit[r2][c2] = 0, 0, 0
        j = 0


dfs(0, 0, 0)
print(answer)