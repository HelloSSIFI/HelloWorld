from copy import deepcopy as dc


def solution(key, lock):
    n, m = len(key), len(lock)

    line = [[0]*(2*n-2+m) for _ in range(n-1)]
    lock = dc(line)+[[0]*(n-1)+lock[i][:]+[0]*(n-1) for i in range(m)]+dc(line)

    def check():
        for r in range(m):
            for c in range(m):
                if now[r+n-1][c+n-1]==0:
                    return False
        return True

    for _ in range(4):      # 회전은 총 3번
        now = dc(lock)

        a, b = 0, 0
        while a < m:
            for i in range(n):
                for j in range(n):
                    if n-1 <= i+a <= n+m-2 and n-1 <= j+b <= n+m-2:
                        now[i+a][j+b] += key[i][j]

            if check():
                return True

            b += 1
            if b == n:
                a += 1
                b = 0

        key = list(map(list, zip(*key[::-1])))

    return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))