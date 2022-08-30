import sys
input = sys.stdin.readline
'''
result = ''
for tc in range(4):
    arr = list(map(int, input().split()))
    win, draw, lose = 0, 0, 0
    total = 0
    for idx in range(0, 16, 3):
        w, d, l = arr[idx], arr[idx+1], arr[idx+2]
        if w+d+l != 5:
            result += '0'
            break
        win += w

        lose += l

        draw = abs(draw-d)
    else:
        if win == lose and draw==0:
            result += '1'
        else:
            result += '0'

print(*result)
'''
from itertools import combinations

# 백트래킹
def dfs(depth):
    global cnt

    # 15번째 경기에 도달했을 때
    if depth == 15:
        cnt = 1
        for sub in arr:
            # 전체 승무패의 합계가 0이 아니면
            if sub.count(0) != 3:
                cnt = 0
                break
        return

    # 전체 경기 15번의 조합
    g1, g2 = games[depth]
    # 각 경기의 승무패
    for x, y in ((0, 2), (1, 1), (2, 0)):
        if arr[g1][x] > 0 and arr[g2][y] > 0:
            arr[g1][x] -= 1
            arr[g2][y] -= 1
            dfs(depth+1)
            arr[g1][x] += 1
            arr[g2][y] += 1


result = []
games = list(combinations(range(6), 2))

for _ in range(4):
    tmp = list(map(int, input().split()))
    arr = [tmp[i:i+3] for i in range(0, 16, 3)]
    cnt = 0
    dfs(0)
    result.append(cnt)

print(*result)