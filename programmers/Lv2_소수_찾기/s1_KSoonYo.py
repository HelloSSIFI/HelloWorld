from itertools import permutations
import math

def solution(numbers):
    answer = 0
    nums = set()

    numbers = list(numbers)
    for i in range(1, len(numbers) + 1):
        perms = list(permutations(numbers, i))
        for perm in perms:
            num = int(''.join(perm))

            if num in nums or num <= 1:
                continue

            is_prime = True
            for j in range(2, int(math.sqrt(num)) + 1):
                if num % j:
                    continue
                else:
                    is_prime = False
                    break
            if is_prime:
                nums.add(num)
    answer = len(nums)
    return answer

solution('1234567')