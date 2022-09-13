def solution(B, Y):
    y = 1
    while y < 2000002:
        if -(B+Y) == y*(y-(B+4)//2):
            return [(B+Y)//y, y]
        y += 1
    return 0


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))