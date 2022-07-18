def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort()
    print(numbers)
    return

solution([3, 30, 34, 5, 9])