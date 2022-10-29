class Node:
    hanging = False

    def __init__(self, t, b, l, r):
        # 인접 상하좌우: 격자 밖이면 -1, 벽이면 0, 빈칸이면 1
        self.t = None
        self.b = None
        self.l = None
        self.r = None


# 행 열 길이
n, m = map(int, input().split())

frame = [input() for _ in range(n)]

