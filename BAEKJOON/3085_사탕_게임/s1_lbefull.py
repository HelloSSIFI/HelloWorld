def check(r, c, d):
    global result
    if d == 0:
        cnt = 1
        for j in range(1, N):                               # 행이 바뀐 경우 해당 행 1줄과
            if arr[r][j - 1] == arr[r][j]:
                cnt += 1
            else:
                cnt = 1
            result = max(result, cnt)
        
        for i in range(2):                                  # 바뀐 열 2줄을 탐색하여 result 갱신
            cnt = 1
            for j in range(1, N):
                if arr[j - 1][c - i] == arr[j][c - i]:
                    cnt += 1
                else:
                    cnt = 1
                result = max(result, cnt)
    
    if d == 1:
        cnt = 1
        for i in range(1, N):                               # 열이 바뀐 경우 해당 열 1줄과
            if arr[i - 1][c] == arr[i][c]:
                cnt += 1
            else:
                cnt = 1
            result = max(result, cnt)
        
        for i in range(2):                                  # 바뀐 행 2줄을 탐색
            cnt = 1
            for j in range(1, N):
                if arr[r - i][j - 1] == arr[r - i][j]:
                    cnt += 1
                else:
                    cnt = 1
                result = max(result, cnt)


N = int(input())
arr = [list(input()) for _ in range(N)]
result = 1
for i in range(N):
    cnt = 1
    cnt2 = 1
    for j in range(1, N):                       # 초기 상태에서 가장 긴 부분을 탐색
        if arr[i][j - 1] == arr[i][j]:          # N이 3 이상이므로 초기상태에서 제일 큰 값이 정답이 될 수 있음
            cnt += 1
        else:
            cnt = 1
        
        if arr[j - 1][i] == arr[j][i]:
            cnt2 += 1
        else:
            cnt2 = 1
        
        result = max(result, cnt, cnt2)

for i in range(N):                              # 바꿀 수 있는 부분이 있으면 바꾸고 바뀐 줄만 탐색하여 result 갱신
    for j in range(1, N):                       # 행을 바꿀 경우 check함수의 3번째 인자로 0을 넘겨주고 열일 경우 1을 넘겨줌
        if arr[i][j - 1] != arr[i][j]:
            arr[i][j - 1], arr[i][j] = arr[i][j], arr[i][j - 1]
            check(i, j, 0)
            arr[i][j - 1], arr[i][j] = arr[i][j], arr[i][j - 1]
        
        if arr[j - 1][i] != arr[j][i]:
            arr[j - 1][i], arr[j][i] = arr[j][i], arr[j - 1][i]
            check(j, i, 1)
            arr[j - 1][i], arr[j][i] = arr[j][i], arr[j - 1][i]

print(result)
