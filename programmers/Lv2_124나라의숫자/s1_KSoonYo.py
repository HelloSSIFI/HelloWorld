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

## 상백님 풀이
'''
def solution(n):
    n -= 1
    if n < 3:
        return '124'[n]
    else:
        q, r = divmod(n, 3)
        return solution(q) + '124'[r]

'''
