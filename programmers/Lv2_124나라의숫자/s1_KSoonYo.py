def solution(n):
    temp = ''
    answer = ''

    while n > 3:
        if n % 3 == 0:
            rest = n - (3 * (n // 3 - 1))
            n = n // 3 - 1
        else:
            rest = n % 3
            n //= 3

        temp = str(rest) + temp
        
    temp = str(n) + temp
    answer = temp.replace('3', '4')
    return answer

