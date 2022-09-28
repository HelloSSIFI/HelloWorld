def dfs(c, total, num):
    global cnt
    if c == total:                          # 모든 자리수를 골랐다면
        cnt += 1                            # cnt + 1
        if cnt == N:                        # 만약 N번째 수가 되었다면 출력
            print(num)
            exit()
        return
    
    for i in range(num % 10):               # 마지막 자리수보다 작아야하므로 num % 10까지 반복
        dfs(c + 1, total, num * 10 + i)     # 재귀


N = int(input())
if N < 11:                                  # 한자리 수이면
    print(N - 1)                            # 0부터 시작하므로 N-1 출력
    exit()

cnt = 10                                    # 위에서 10까지 찾았으므로 초기값 10
for i in range(2, 11):                      # 두자리 수부터 최고자리인 10자리(9876543210) 까지 반복
    for j in range(1, 10):                  # 맨 앞자리는 0이 들어갈 수 없으므로 1~9
        dfs(1, i, j)

print(-1)
