M = int(input())
N = int(input())

def search(n):
    cnt = 0

    for i in range(n, 0, -1):
        if not n%i:
            cnt += 1
    if cnt == 2:
        return 1
    return 0


result = 0
min_v = 100
for num in range(N, M-1, -1):
    if search(num):
        result += num
        min_v = num

if result:
    print(result)
    print(min_v)
else:
    print(-1)