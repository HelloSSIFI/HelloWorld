N = 3
M = 7

cnt = 2
var = 1
result = 0

while var < N:
    var += cnt
    cnt += 1

else:
    if N - var > M- N + 1:
        result = cnt*(N-1) + (M-N+1-var)*(cnt+1)
    else:
        result = cnt * (N - 1)

print(result)