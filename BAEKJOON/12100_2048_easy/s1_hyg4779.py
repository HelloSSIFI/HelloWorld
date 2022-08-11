import copy
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
answer = 0


def up(mat=list):
    flag = True

    while flag:
        flag = False

        for i in range(n-1):
            for j in range(n):
                if 0 != mat[i][j] == mat[i+1][j] and mat[i][j]%2 == 0 :
                    mat[i][j], mat[i+1][j] = mat[i][j]*2, 0


                pass
    return mat


def down(mat=list):
    flag = True

    while flag:
        flag = False

        for i in range(n-1):
            for j in range(n):
                if 0 != mat[i][j] == mat[i+1][j]:
                    mat[i][j]
                pass
    return mat


def left(mat=list):
    flag = True

    while flag:
        flag = False

        for i in range(n-1):
            for j in range(n):
                if 0 != mat[i][j] == mat[i+1][j]:
                    mat[i][j]
                pass
    return mat


def right(mat=list):
    flag = True

    while flag:
        flag = False

        for i in range(n-1):
            for j in range(n):
                if 0 != mat[i][j] == mat[i+1][j]:
                    mat[i][j]
                pass
    return mat


def solution(cnt=int, now=list):
    if cnt == 5:
        return

    u_new = up(copy.deepcopy(now))
    d_new = down(copy.deepcopy(now))
    l_new = left(copy.deepcopy(now))
    r_new = right(copy.deepcopy(now))
    solution(cnt+1, u_new)
    solution(cnt+1, d_new)
    solution(cnt+1, l_new)
    solution(cnt+1, r_new)

solution(0, arr)