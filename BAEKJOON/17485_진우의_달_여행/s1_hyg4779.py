import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]

answer = 100001

'''
0행부터 다음 행으로 넘어갈 때,
-1, 0, 1씩 더한 위치(이전에 이동한 방향제외) 중 가장 작은 값으로 이동
'''

def recur(r, c, now, head):
    global answer

    if now > answer:
        return

    if r == n:
        if answer > now:
            answer = now
        return

    next = []
    for j in head:
        # 다음 위치 값, 열번호, 이동방향
        if 0 <= c+j < m:
            next.append((field[r][c+j], c+j, j))

    for move in next:
        nhead = [-1, 0, 1]
        # 현재 이동방향 제외
        nhead.pop(nhead.index(move[2]))

        # 다음 층으로 이동
        # 다음 층, 다음 열번호, 현재 까지 연료량, 다음 이동할 수 있는 방향
        recur(r+1, move[1], now+move[0], nhead)


for i in range(m):
    recur(1, i, field[0][i], [-1, 0, 1])

print(answer)