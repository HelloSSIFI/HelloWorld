from collections import deque


def solution(beginning, target):
    answer = 0

    n, m = len(beginning), len(beginning[0])
    vis_r, vis_c = [0]*n, [0]*m

    for i in range(n):
        for j in range(m):

            if beginning[i][j] != target[i][j] and not vis_r[i] and not vis_c[j]:
                vis_r[i], vis_c[j] = 1, 1
                Q = deque([([[line[::] for line in beginning]], i, j, vis_r, vis_c, 0)])

                while Q:
                    arr, r, c, vr, vc, cnt = Q.popleft()



    return answer