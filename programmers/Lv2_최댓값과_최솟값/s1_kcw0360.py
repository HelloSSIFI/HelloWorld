def solution(s):
    numbers = list(map(int, s.split()))
    return '{} {}'.format(min(numbers), max(numbers))