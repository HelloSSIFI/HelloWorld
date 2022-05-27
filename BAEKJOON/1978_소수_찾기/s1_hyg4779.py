T = int(input())

arr = list(map(int, input().split()))

def search(n):
    cnt = 0

    for i in range(n, 0, -1):
        if not n%i:
            cnt += 1
    if cnt == 2:
        return 1
    return 0

count = 0

for num in arr:
    if search(num):
        count += 1

print(count)