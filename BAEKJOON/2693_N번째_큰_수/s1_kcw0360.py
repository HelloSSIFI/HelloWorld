A = int(input())

for _ in range(A):
    numbers = sorted(list(map(int, input().split())))
    print(numbers[-3])
