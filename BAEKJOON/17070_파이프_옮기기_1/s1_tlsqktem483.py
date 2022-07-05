"""
시간초과
"""
import sys


def dfs(n, room):
    di = [[[(0, 1), (0, 1)], [(1, 1), (0, 1)]], [[(1, 0), (1, 0)], [(1, 1), (1, 0)]], [[(0, 1), (1, 1)], [(1, 0), (1, 1)], [(1, 1), (1, 1)]]]
    stack = [[(0, 1), (0, 0)]]
    cnt = 0
    d_idx = 0

    while stack:
        h, t = stack.pop()
        if h == (n, n):
            cnt += 1
            continue
        # 가로
        if h[0] == t[0] and h[1] == t[1]+1:
            d_idx = 0
        # 세로
        elif h[1] == t[1] and h[0] == t[0]+1:
            d_idx = 1
        # 대각선
        elif h[1] == t[1]+1 and h[0] == t[0]+1:
            d_idx = 2

        # 예외처리
        if d_idx == 0 and h[1] == n:
            continue
        elif d_idx == 1 and h[0] == n:
            continue

        for d in di[d_idx]:
            d_h, d_t = d[0], d[1]
            next_h, next_t = (h[0]+d_h[0], h[1]+d_h[1]), (t[0]+d_t[0], t[1]+d_t[1])

            if 0 <= next_h[0] <= n and 0 <= next_h[1] <= n and not room[next_h[0]][next_h[1]]:
                # 대각선 벽 확인
                if next_h[0] == next_t[0]+1 and next_h[1] == next_t[1]+1:
                    if not room[next_h[0]][next_h[1]-1] and not room[next_h[0]-1][next_h[1]]:
                        stack.append([next_h, next_t])
                else:
                    stack.append([next_h, next_t])
    return cnt


N = int(sys.stdin.readline())
p_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(dfs(N-1, p_map))