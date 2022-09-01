def dfs(a, b, c, prev):

    # a, b, c의 개수가 초기 카운트와 같으면 찾은 것
    if a == ac and b == bc and c == cc:
        print(''.join(answer))
        exit(0)

    if dp[a][b][c][prev[0]][prev[1]]:
        return False

    dp[a][b][c][prev[0]][prev[1]] = True

    # A개수 만큼 사용하지 않았다면
    if a < ac:
        answer[a+b+c] = 'A'
        if dfs(a+1, b, c, [prev[1], A]):
            return True

    # B개수 만큼 사용하지 않았다면
    if b < bc:
        answer[a+b+c] = 'B'
        # 전날에 선택한 것이 B가 아니라면
        if prev[1] != B:
            if dfs(a, b+1, c, [prev[1], B]):
                return True

    # C개수 만큼 사용하지 않았다면
    if c < cc:
        answer[a+b+c] = 'C'
        # 전전날과 전날에 선택한 것이 C가 아니라면
        if prev[0] != C and prev[1] != C:
            if dfs(a, b, c+1, [prev[1], C]):
                return True

    return False



A, B, C = 0, 1, 2
S = input()
length = len(S)
answer = [''] * length

ac, bc, cc = 0, 0, 0

for s in S:
    if s=='A':
        ac += 1
    elif s=='B':
        bc += 1
    else:
        cc += 1

dp = [[[[[False for _ in range(3)] for _ in range(3)] for _ in range(length)] for _ in range(length)] for _ in range(length)]
dfs(0, 0, 0, [0, 0])
print(-1)