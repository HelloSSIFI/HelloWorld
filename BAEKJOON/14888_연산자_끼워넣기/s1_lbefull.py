def dfs(cnt, s):
    global result_max, result_min

    if cnt == N:                            # 모든 수로 연산을 했으면
        result_max = max(result_max, s)     # 결과 갱신
        result_min = min(result_min, s)
        return
    
    for i in range(4):                      # 연산자 순회
        if oper[i]:                         # 연산자 사용 횟수가 남았으면
            oper[i] -= 1                    # 횟수 -1
            if i == 0:                      # 연산자에 맞게 연산 후 재귀
                dfs(cnt + 1, s + A[cnt])
            elif i == 1:
                dfs(cnt + 1, s - A[cnt])
            elif i == 2:
                dfs(cnt + 1, s * A[cnt])
            else:
                if s < 0:
                    dfs(cnt + 1, -(-s // A[cnt]))
                else:
                    dfs(cnt + 1, s // A[cnt])
            oper[i] += 1                    # 다시 횟수 +1


N = int(input())
A = list(map(int, input().split()))
oper = list(map(int, input().split()))
result_max = -100000000                     # 결과 초기화
result_min = 100000000

dfs(1, A[0])                                # 처음수를 넣어주고 재귀

print(result_max)
print(result_min)
