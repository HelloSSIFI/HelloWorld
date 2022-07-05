from itertools import permutations


def calc(num1, num2, oper):                 # 연산자에 맞게 두 수를 계산하여 반환
    if oper == '+':
        return num1 + num2
    if oper == '-':
        return num1 - num2
    if oper == '*':
        return num1 * num2


def dfs(opers, num_list, oper_list):
    global answer
    if len(num_list) == 1:                              # 더이상 연산이 없으면
        answer = max(answer, abs(num_list[0]))          # answer 갱신
        return
    
    num_list_copy = num_list[:]
    oper_list_copy = oper_list[:]

    flag = False
    for oper in opers:                                  # 입력받은 연산자 순서대로
        for i in range(len(oper_list)):                 # 해당 연산을 먼저 수행하고 재귀
            if oper_list[i] == oper:
                flag = True
                num1 = num_list_copy.pop(i)
                num2 = num_list_copy.pop(i)
                num_list_copy.insert(i, calc(num1, num2, oper_list_copy.pop(i)))
                dfs(opers, num_list_copy, oper_list_copy)
                break
        
        if flag:
            break


def solution(expression):
    global answer
    answer = 0

    temp = ''
    num_list = []
    oper_list = []
    for exp in expression:                      # 숫자는 num_list에, 연산자는 oper_list에 담아줌
        if exp in '+-*':
            num_list.append(int(temp))
            temp = ''
            oper_list.append(exp)
        else:
            temp += exp
    num_list.append(int(temp))

    for p in list(permutations('+-*', 3)):      # 나올수 있는 연산자 순서를 반복
        dfs(p, num_list, oper_list)

    return answer


# print(solution("100-200*300-500+20"))
