from math import factorial


def solution(n, k):
    answer = []
    numbers = list(range(1, n + 1))
    cnt = n - 1
    x = factorial(cnt)

    while True:
        a, b = divmod(k, x)
        if b == 0:
            answer.append(numbers[a - 1])
            numbers.pop(a - 1)
            break
        else:
            answer.append(numbers[a])
        numbers.pop(a)
        k = b
        x //= cnt
        cnt -= 1

    if len(numbers) != 0:
        for i in range(len(numbers) - 1, -1, -1):
            answer.append(numbers[i])

    return answer
