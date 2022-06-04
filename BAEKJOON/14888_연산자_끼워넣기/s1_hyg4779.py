N = int(input())            # 수의 개수
nums = list(map(int, input().split()))      # N개의 수 배열
operators = list(map(int, input().split())) # 연산자 idx 0: +, idx 1: -, idx 2: *, idx: 3: //

def dfs(idx, val, opers):               # dfs 순회
    global min_v, max_v

    if idx == N:                        # 최대, 최소값 갱신
        if min_v > val: min_v = val
        if max_v < val: max_v = val
        return

    new_opers = opers[::]               # 연산자 배열을 그대로 쓰면 계속해서 참조하기 때문에, 복사 후 사용

    for i in range(4):                  # 연산자 종류 4가지
        if new_opers[i] > 0:
            new_opers[i] -= 1

            if i == 0:
                dfs(idx+1, val+nums[idx], new_opers)

            elif i == 1:
                dfs(idx+1, val-nums[idx], new_opers)

            elif i == 2:
                dfs(idx+1, val*nums[idx], new_opers)

            elif i == 3:
                if val >= 0:
                    dfs(idx+1, val//nums[idx], new_opers)
                else:
                    dfs(idx+1, (-val//nums[idx])*(-1), new_opers)

            new_opers[i] += 1


min_v = float('INF')
max_v = float('-INF')
value = nums[0]

dfs(1, value, operators)
print(max_v)
print(min_v)