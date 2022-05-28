N = int(input())
arr = map(int, input().split())
ans = 0

for n in arr:
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    if flag and n != 1:
        ans += 1
print(ans)