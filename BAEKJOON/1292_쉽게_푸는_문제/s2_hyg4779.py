N, M = map(int, input().split())


cnt = 0
tmp = 0

while tmp < N:
    cnt += 1
    tmp += cnt


result = 0
result += cnt*(tmp-N+1)


while tmp < M:
    cnt += 1
    result += cnt*cnt
    tmp += cnt

result -= cnt*(tmp-M)

print(result)