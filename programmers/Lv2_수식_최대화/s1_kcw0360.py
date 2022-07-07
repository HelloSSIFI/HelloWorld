from itertools import permutations


def cal(per, numbers, operator, origin):
    numbers = numbers
    operator = operator

    # 우선순위대로 idx가 빠르게 하여 연산자 리스트 생성
    op = [origin[per[0]], origin[per[1]], origin[per[2]]]

    # op 리스트의 idx 순서대로 연산자 우선 계산
    for i in range(len(op)):
        stack = []
        stack.append(numbers[0])
        temp_op = []

        # op에서 꺼내온 연산자랑 operator를 순회하며 비교후 같다면 연산함.
        for j in range(len(operator)):
            if op[i] == operator[j]:
                k = stack.pop()
                if op[i] == '*':
                    temp = k * numbers[j+1]
                    stack.append(temp)
                elif op[i] == '+':
                    temp = k + numbers[j+1]
                    stack.append(temp)
                else:
                    temp = k - numbers[j+1]
                    stack.append(temp)
            else:
                temp_op.append(operator[j])
                stack.append(numbers[j+1])
        numbers = stack
        operator = temp_op

    return abs(numbers[0])


def solution(expression):
    origin = ['*', '+', '-']
    numbers = []
    operator = []
    temp = ''
    result = []

    # 숫자와 연산자 분리해주기
    for i in expression:
        if i.isdigit():
            temp += i
        else:
            numbers.append(int(temp))
            temp = ''
            operator.append(i)
    numbers.append(int(temp))

    # 우선순위 경우의수 조회하기(origin으로)
    for per in permutations(range(len(origin)), 3):
        # 우선순위 순서대로 연산한 후 결과값을 result에 절대값으로 저장
        result.append(cal(per, numbers, operator, origin))

    answer = max(result)

    return answer