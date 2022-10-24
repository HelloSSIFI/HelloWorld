N = int(input())
arr = []
all_people = 0

for _ in range(N):
    x, a = map(int, input().split())
    arr.append([x, a])
    all_people += a

arr.sort(key=lambda x: x[0])

ans = 0
pre_sum = 0
for loc, people in arr:
    pre_sum += people

    if pre_sum >= all_people/2:
        ans = loc
        break
print(ans)
