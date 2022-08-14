from copy import deepcopy as dc
import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def up(mat=list):
    for j in range(n):
        pointer = 0
        for i in range(1, n):
            if mat[i][j]:
                tmp = mat[i][j]
                mat[i][j] = 0

                if mat[pointer][j] == 0:
                    mat[pointer][j] = tmp
                elif mat[pointer][j] == tmp:
                    mat[pointer][j] *= 2
                    pointer += 1
                else:
                    pointer += 1
                    mat[pointer][j] = tmp

    return mat


def down(mat=list):

    for j in range(n):
        pointer = n-1
        for i in range(n-2, -1, -1):
            if mat[i][j]:
                tmp = mat[i][j]
                mat[i][j] = 0
                if mat[pointer][j] == 0:
                    mat[pointer][j] = tmp
                elif mat[pointer][j] == tmp:
                    mat[pointer][j] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    mat[pointer][j] = tmp

    return mat


def left(mat=list):
    for i in range(n):
        pointer = 0
        for j in range(1, n):
            if mat[i][j]:
                tmp = mat[i][j]
                mat[i][j] = 0
                if mat[i][pointer] == 0:
                    mat[i][pointer] = tmp
                elif mat[i][pointer] == tmp:
                    mat[i][pointer] *= 2
                    pointer += 1
                else:
                    pointer += 1
                    mat[i][pointer] = tmp

    return mat


def right(mat=list):
    for i in range(n):
        pointer = n-1
        for j in range(n-2, -1, -1):
            if mat[i][j]:
                tmp = mat[i][j]
                mat[i][j] = 0
                if mat[i][pointer] == 0:
                    mat[i][pointer] = tmp
                elif mat[i][pointer] == tmp:
                    mat[i][pointer] *= 2
                    pointer -= 1
                else:
                    pointer -= 1
                    mat[i][pointer] = tmp
    return mat


def solution(cnt=int, now=list):
    global answer
    if cnt == 5:
        for r in range(n):
            for c in range(n):
                answer = max(answer, now[r][c])
        return

    u_new = up(dc(now))
    d_new = down(dc(now))
    l_new = left(dc(now))
    r_new = right(dc(now))

    solution(cnt+1, u_new)
    solution(cnt+1, d_new)
    solution(cnt+1, l_new)
    solution(cnt+1, r_new)
    return

answer = 0
solution(0, arr)

print(answer)