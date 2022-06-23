import sys
input = sys.stdin.readline

N = int(input())                                        # NxN 행렬
arr = [list(input()) for _ in range(N)]         # 사탕 배열



def check(mat):
    r_cnt = c_cnt = 1

    answer = 0
    for i in range(N):
        for j in range(N-1):
            if mat[i][j] == mat[i][j+1]:
                r_cnt += 1
            else:
                r_cnt = 1

            if mat[j][i] == mat[j+1][i]:
                c_cnt += 1
            else:
                c_cnt = 1

        answer = max(r_cnt, c_cnt, answer)
        r_cnt = c_cnt = 1

    return answer

ans = 0

for i in range(N):
    for j in range(N):

        if j < N-1 and arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
            tmp = check(arr)
            ans = max(tmp, ans)
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        if i < N-1 and arr[i][j] != arr[i+1][j]:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
            tmp = check(arr)
            ans = max(tmp, ans)
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]


print(ans)