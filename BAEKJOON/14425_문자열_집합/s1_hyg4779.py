n, m = map(int, input().split())
S = {input().rstrip(): 0 for _ in range(n)}
arr = [input().rstrip() for _ in range(m)]

result = 0
for word in arr:
    if S.get(word)==None:
        continue
    result += 1

print(result)