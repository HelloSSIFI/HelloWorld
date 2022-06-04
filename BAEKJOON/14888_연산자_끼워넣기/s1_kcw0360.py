def dfs(idx, result, add, sub, mul, div):
    global max_result, min_result

    if idx == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return

    if add:
        dfs(idx + 1, result + numbers[idx], add - 1, sub, mul, div)
    if sub:
        dfs(idx + 1, result - numbers[idx], add, sub - 1, mul, div)
    if mul:
        dfs(idx + 1, result * numbers[idx], add, sub, mul - 1, div)
    if div:
        if result < 0:
            dfs(idx + 1, -((-result) // numbers[idx]), add, sub, mul, div - 1)
        else:
            dfs(idx + 1, result // numbers[idx], add, sub, mul, div - 1)

N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_result = -(10**10)
min_result = 10**10

dfs(1, numbers[0], add, sub, mul, div)

print(max_result)
print(min_result)