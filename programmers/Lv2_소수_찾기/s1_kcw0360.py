from itertools import permutations


def check(numbers):
    temp = ''
    for i in numbers:    # 숫자로 만들기
        temp += i
    temp = int(temp)

    if temp == 1:    # 1인 경우 소수가 아니므로 걸러주기
        return 0

    for i in range(2, temp//2 + 1):    # 소수찾기
        if temp % i == 0:    # 소수가 아닌 경우
            return 0

    return temp


def solution(numbers):
    result = set()
    numbers = list(numbers)
    for i in range(1, len(numbers) + 1):
        for j in permutations(numbers, i):    # 종이조각으로 만들 수 있는 모든 경우 찾기
            k = check(j)
            if k != 0:    # 소수인 경우 result에 추가
                result.add(k)

    return len(result)