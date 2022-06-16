S = int(input())

res = 1

while True:
    check = res * (res+1) // 2

    if check > S:
        break

    res += 1

print(res - 1)