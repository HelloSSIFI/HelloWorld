start, end = map(int, input().split())


numbers = []

for i in range(1000):
    temp = [i] * i
    numbers += temp

print(sum(numbers[start-1:end]))
