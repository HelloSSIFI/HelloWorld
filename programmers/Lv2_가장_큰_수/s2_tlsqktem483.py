def solution(numbers):
    sorted_numbers = list(map(str, numbers))
    sorted_numbers.sort(key=lambda x: x*3, reverse=True)

    return str(int(''.join(sorted_numbers)))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))