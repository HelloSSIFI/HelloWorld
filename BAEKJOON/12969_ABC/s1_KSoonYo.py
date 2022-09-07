
N, K = map(int, input().split())

def solution(i, a, b, k, ans = ''):
    if i == N:
        if k == K:
            return ans
        return None

    if dp[i][a][b][k]:                  # back
        return None

    dp[i][a][b][k] = True

    # A를 붙이는 경우
    # 문자열 길이와 a 개수는 늘어나지만 A가 가장 작기 때문에 순서쌍은 늘어나지 않음
    case1 = solution(i + 1, a + 1, b, k, ans + 'A')
    if case1:
        return case1

    # B를 붙이는 경우
    # 앞에 a가 있는 개수 만큼 순서쌍이 늘어남( A < B 이므로)
    case2 = solution(i + 1, a, b + 1, k + a, ans + 'B')
    if case2:
        return case2

    # C를 붙이는 경우
    # 앞에 a와 b가 있는 개수 만큼 순서쌍이 늘어남 ( A < B < C 이므로)
    case3 = solution(i + 1, a, b, k + a + b, ans + 'C')
    if case3:
        return case3
    
    return None

# dp[문자열 길이][A의 개수][B의 개수][순서쌍의 개수] , C의 개수는 문자열 길이에서 A의 개수와 B의 개수를 뺀 경우
# 문자열 길이 i일 때 A의 개수 ?, B의 개수 ?, C의 개수 (i - A + B), 순서쌍 k개일 때 문자열 생성 가능 여부

# 시간초과
# dp = []
# for i in range(N + 1):
#     dp.append([])
#     for a in range(N + 1):
#         dp[i].append([])
#         for b in range(N + 1):
#             dp[i][a].append([])
#             for j in range(K * (K - 1) // 2 + 1):
#                 dp[i][a][b].append(False)

dp = [[[[False for _ in range(N * (N - 1) // 2)] for _ in range(N)] for _ in range(N)] for _ in range(N)]


result = solution(0, 0, 0, 0)
if result:
    print(result)
else:
    print(-1)



