from itertools import permutations


def check(number):
    if number in [0, 1]:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False

    return True


def solution(numbers):
    answer = []
    numbers = list(numbers)

    for i in range(1, len(numbers) + 1):
        for n in permutations(numbers, i):
            temp = ''
            for j in n:
                temp += j
            temp = int(temp)
            if check(temp) and temp not in answer:
                answer.append(temp)
    return len(answer)


print(solution("17"))
print(solution("011"))
