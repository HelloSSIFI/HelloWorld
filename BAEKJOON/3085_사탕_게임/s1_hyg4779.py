N = int(input())                            # NxN 행렬
arr = [list(input()) for _ in range(N)]     # 사탕 배열


def check(mat):
    r_cnt = c_cnt = 1                       # r_cnt, c_cnt: 행&열별 가장 길게 연결된 사탕을 세는 변수

    answer = 0                              # 가장 큰 값 return할 변수
    for i in range(N):
        for j in range(N-1):
            if mat[i][j] == mat[i][j+1]:    # 행에서 연속되면 +1
                r_cnt += 1
            else:                           # 다르면 1
                r_cnt = 1

            if mat[j][i] == mat[j+1][i]:    # 열에서 연속되면 +1
                c_cnt += 1
            else:                           # 다르면 1
                c_cnt = 1

        answer = max(r_cnt, c_cnt, answer)  # 최댓값 갱신
        r_cnt = c_cnt = 1                   # 카운트 개수 초기화

    return answer

ans = 0

for i in range(N):
    for j in range(N):

        if j < N-1 and arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j] # 행 교환
            tmp = check(arr)
            ans = max(tmp, ans)
            arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j] # 원 위치

        if i < N-1 and arr[i][j] != arr[i+1][j]:
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j] # 열 교환
            tmp = check(arr)
            ans = max(tmp, ans)
            arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j] # 원 위치


print(ans)