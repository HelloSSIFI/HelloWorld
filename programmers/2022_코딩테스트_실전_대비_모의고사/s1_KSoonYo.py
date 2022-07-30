def solution(X, Y):
    answer = ''
    x = set(X)
    y = set(Y)
    pair = x & y
    numbers = []

    if len(pair) == 0:
        answer = '-1'
        return answer
    elif len(pair) == 1 and '0' in pair:
        answer = '0'
        return answer
    
    for num in pair:
        if X.count(num) >= Y.count(num):
            numbers += [num] * Y.count(num)
        else:
            numbers += [num] * X.count(num)
    
    numbers.sort(reverse=True)
    answer = ''.join(numbers)
    return answer

solution('3403', '13203')
solution('5525', '1255')
solution('12345', '534')