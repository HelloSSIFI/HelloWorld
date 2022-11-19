# pypy3 통과
N = int(input())

stack = [1]                                                  # 사면체를 만들 때 필요한 대포알 개수 stack
triangle_stack = [1]                                         # 삼각형 대포알 stack

# 대포알 1개짜리 정사면체로 i개 대포알이 필요한 만큼의 정사면체 개수로 만들 수 있으므로 해당 개수로 초기화
dp = [i for i in range(N + 1)]                              # dp[i] : i개 대포알로 만들 수 있는 최소 정사면체 개수

i = 2
while True:
    triangle_stack.append(triangle_stack[-1] + i) 
    new_sph = stack[-1] + triangle_stack[-1]
    if new_sph > N:
        break
    stack.append(new_sph)
    dp[stack[-1]] = 1                                        # stack[-1]가 곧 사면체이므로 dp에서 해당 대포알 인덱스의 값을 1개로 설정                                               
    i += 1

for j in range(2, N + 1):
    if dp[j] == 1:
        continue

    for sph in stack:
        if j - sph > 0:                                     # 이전에 기록된 j개짜리 사면체 개수 vs j개 대포알에서 사면체에 해당하는 대포알 sph 개수를 뺀 나머지 대포알에 필요한 사면체 개수 + 1
            dp[j] = min(dp[j], dp[j - sph] + 1)
        else:
            break
        
print(dp[N])


# 계차수열 공식을 이용한 solution
N = int(input())

stack = []                                                  # 사면체를 만들 때 필요한 대포알 개수 stack

# 대포알 1개짜리 정사면체로 i개 대포알이 필요한 만큼의 정사면체 개수로 만들 수 있으므로 해당 개수로 초기화
dp = [i for i in range(N + 1)]                              # dp[i] : i개 대포알로 만들 수 있는 최소 정사면체 개수

new_sph = 0
i = 1

'''

해설)
각각의 삼각형은 1, 3, 6, 10, ...로 2, 3, 4 ... 씩 증가하는 수열이다.
         수열    2, 3, 4는 1씩 증가하는 등차수열 
삼각형 수열 n항의 값은 첫째항 1에서 2, 3, 4, ... 씩 증가하는 등차수열의 n - 1항까지의 합 
1씩 증가하는 등차수열을 계차로 지니는 수열의 일반항 공식 = (n * (n + 1)) // 2

'''
while new_sph < N:
    new_sph += (i * (i + 1)) // 2    
    if new_sph <= N:
        stack.append(new_sph) 
        dp[new_sph] = 1                                        # new_sph가 곧 사면체이므로 dp에서 new_sph 자리의 값을 1개로 설정(사면체 1개 필요)                                               
    i += 1

for j in range(1, N + 1):
    if dp[j] == 1:
        continue

    for sph in stack:
        # min()으로 최소값 갱신하면 시간초과
        if j - sph > 0 and dp[j] > dp[j - sph] + 1:                                     # 이전에 기록된 j개짜리 사면체 개수 vs j개 대포알에서 사면체에 해당하는 대포알 sph 개수를 뺀 나머지 대포알에 필요한 사면체 개수 + 1
            dp[j] = dp[j - sph] + 1
        
print(dp[N])


