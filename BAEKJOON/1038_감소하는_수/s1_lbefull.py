def dfs(l, pre, s):
    '''
    l : 재귀 횟수
    pre : 이전 재귀의 숫자
    s : 만들어진 수
    '''
    global cnt, result
    if l == i:                  # 만약 i번 골랐다면
        cnt += 1                # cnt 1 증가
        if cnt == N:            # 현재 수가 N번째 숫자이면
            result = s          # 저장
        return
    
    for k in range(0, pre):
        dfs(l + 1, k, s + k * 10 ** (i - l - 1))


N = int(input())
cnt = -1
result = -1

for i in range(10):                 # 감소하는 수는 9876543210 보다 큰 수는 없으므로 최대 길이는 10
    for j in range(10):
        if i > 0 and j == 0:        # 한 자리 수를 제외하면 맨 앞에 0 이 올 수 없으므로 continue
            continue
        dfs(0, j, j * 10 ** i)

print(result)
