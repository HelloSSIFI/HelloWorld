def is_prime(n):
    n = int(n)
    if n == 1:
        return False
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False
    return True


def change(n, k):
    temp = ''

    while n > 0:
        n, m = divmod(n, k)
        temp += str(m)
    return temp[::-1]


def solution(n, k):
    changed_n = change(n, k)
    answer = 0
    current = ''

    for i in range(len(changed_n)):
        num = changed_n[i]
        if num == '0' and not current:
            continue
        elif num == '0' and current:
            if is_prime(current):
                answer += 1
            current = ''
        elif i == len(changed_n)-1:
            current += num
            if is_prime(current):
                answer += 1
        else:
            current += num

    return answer