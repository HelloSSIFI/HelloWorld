def solution(numbers):

    N = len(numbers)
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x:x*3, reverse=True)
    return str(int(''.join(numbers)))

# https://jokerldg.github.io/algorithm/2021/05/06/most-big-number.html