

minumum_prime = [2, 3, 5, 7, 11]

def update_prime(max_number):
    for num in range(12, max_number + 1):
        if is_prime(num) and num not in minumum_prime:
            minumum_prime.append(num)


def is_prime(num):
    if num == 1:
        return False

    if num in minumum_prime:
        return True
    
    for idx in range(len(minumum_prime)):
        if num % minumum_prime[idx]:
            continue
        else:
            return False  

    return True


N = int(input())
number_list = list(map(int, input().split()))
count = 0

update_prime(max(number_list))

for number in number_list:
    if is_prime(number):
        count += 1


print(count)
