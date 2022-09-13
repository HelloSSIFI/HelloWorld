def solution(number, k):
    answer = ''

    origin_K = k
    for idx in range(len(number)):
        if number[idx] == '9' or not k:
            answer += number[idx]
            continue

        if k == origin_K and len(number) - idx == k:
            # k가 변함이 없고 남은 숫자의 개수가 k개만큼 있다면
            # 남은 k개를 모두 지워주기만 하면 끝
            break

        comp = number[idx + 1: idx + k + 1]
        flag = True
        for num in comp:
            if int(number[idx]) < int(num):
                flag = False
                k -= 1
                break
        if flag:
            answer += number[idx]
    

    return answer



# best solution
# stack을 이용한 풀이

def best_solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


