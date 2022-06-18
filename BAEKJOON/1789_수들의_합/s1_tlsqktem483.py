s = int(input())

temp = 0
n = 0

for i in range(1, 4294967295):
    temp += i
    n += 1

    if temp > s:
        break

print(n - 1)