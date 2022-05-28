M = int(input())
N = int(input())
prime_number = [1] * 10001
prime_number[0] = 0
prime_number[1] = 0

for i in range(2, 10001):
    if not prime_number[i]:
        continue

    j = 2
    while i * j < 10001:
        prime_number[i * j] = 0
        j += 1

result_min = -1
result_sum = 0
for i in range(N, M - 1, -1):
    if prime_number[i]:
        result_min = i
        result_sum += i

if result_sum:
    print(result_sum)
print(result_min)
