def solution(n):
    answer = ''
    check = {1: '1', 2: '2', 0: '4'}
    while n > 0:
        answer = check[n % 3] + answer
        n = (n-1) // 3
    return answer