M = int(input())
N = int(input())
arr = []

for n in range(M, N + 1):
    flag = 0
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                flag += 1
                break
        if flag == 0:
            arr.append(n)

if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)