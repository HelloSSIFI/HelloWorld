
def get_patterns(temp = []):
    
    if max(operation_count) == 0:
        patterns.append(temp)
        return

    for start in range(0, 4):
        if operation_count[start] > 0:
            temp.append(operations[start])
            operation_count[start] -= 1
            get_patterns(temp[:])

            operation_count[start] += 1
            temp.pop()

N = int(input())


numbers = list(map(int, input().split()))               # 숫자 리스트 입력
operation_count = list(map(int, input().split()))       # 연산자 개수

operations = [
    
    '+', '-', '*', '/'
]                                                       # 연산자 정의

actions = {
    '+' : lambda x, y : x + y,
    '-' : lambda x, y : x - y,
    '*' : lambda x, y : x * y,
    '/' : lambda x, y : x // y
}


patterns = []
result = []
get_patterns()                                          # 가능한 모든 연산자 패턴 구하기(완전탐색)

for pattern in patterns:                                # 패턴 별 연산 시작
    temp = numbers[:]
    number_idx = 0                                      # 숫자 배열의 인덱스
    operation_idx = 0                                   # 패턴 내 연산자를 가리키는 인덱스
    while operation_idx < len(pattern):                 # 패턴 내 연산자를 모두 순회할 때까지 반복
        x, y = temp[number_idx], temp[number_idx + 1]   # x: 현재 가리키는 숫자, y: x 바로 다음에 있는 피연산자
        operation = pattern[operation_idx]              # 패턴 내 현재 연산자

        if operation == '/' and x < 0:                  # 음수를 양수로 나눌 때 C++14 규칙 적용
            x = -x
            temp[number_idx], temp[number_idx + 1] = 0, -actions[operation](x, y)
        else:
            temp[number_idx], temp[number_idx + 1] = 0, actions[operation](x, y)    # 현재 가리키는 숫자 자리는 0으로, 피연산자 자리에 결과값을 누적

        operation_idx += 1
        number_idx += 1

    result.append(temp[-1])                             # 가장 마지막으로 누적된 결과값이 최종 결과값이므로 result에 추가


print(max(result))
print(min(result))
