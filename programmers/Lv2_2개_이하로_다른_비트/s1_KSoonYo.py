
def solution(numbers):
    answer = []
    for number in numbers:
        num1, num2 = number, number + 1
        a = list(format(num1, 'b'))
        b = list(format(num2, 'b'))
        c = format(num1 ^ num2, 'b')
        maxC = c.count('1')
        if maxC <= 2:
            answer.append(int(''.join(b), 2))
            continue
        
        maxL = len(b)
        a = ['0'] * (maxL - len(a)) + a
        for i in range(maxL - 1, -1, -1):
            if a[i] != b[i]:
                b[i] = a[i]
                maxC -= 1
            if maxC <= 2:
                break
        answer.append(int(''.join(b), 2))

    return answer



########
# best solution
########
def solution(numbers):
    answer = []
    for val in numbers:
        answer.append(((val ^ (val+1)) >> 2) +val +1)

    return answer

