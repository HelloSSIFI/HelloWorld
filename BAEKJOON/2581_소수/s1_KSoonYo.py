
minimum_prime = [2, 3, 5, 7, 11]

def is_prime(num):
    if num not in minimum_prime and num < max(minimum_prime):
        return False
    
    if num in minimum_prime:
        return True

    for prime in minimum_prime:
        if num % prime:
            continue
        else:
            return False
    return True


M = int(input())
N = int(input())

numbers = [i for i in range(M, N + 1)]
result = []
for number in range(1, N+1):
    if is_prime(number):
        if number not in minimum_prime:
            minimum_prime.append(number)

        if number >= M:
            result.append(number) 

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)