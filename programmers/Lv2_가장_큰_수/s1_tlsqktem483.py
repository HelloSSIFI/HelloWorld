"""
시간초과
"""
from itertools import permutations


def solution(numbers):
    answer = 0

    for p in permutations(numbers, len(numbers)):
        temp = ''
        for n in p:
            temp += str(n)
        if int(temp) > answer:
            answer = int(temp)
    return str(answer)


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))