target = int(input())

total = 1
num = 1
cnt = 1
while total <= target:
    num += 1
    total += num
    cnt += 1

print(cnt-1)
