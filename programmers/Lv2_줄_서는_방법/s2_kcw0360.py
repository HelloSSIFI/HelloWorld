from math import factorial


def solution(n, k):
    answer = []
    numbers = list(range(1, n + 1))

    while n != 0:
        x = factorial(n - 1)
        answer.append(numbers.pop((k - 1) // x))
        n, k = n - 1, k % x

    return answer
