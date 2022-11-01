from collections import Counter


def solution(topping):
    answer = 0
    check = Counter(topping)    # 철수가 모두 가지고 있다는 것으로 가정하고 토핑 종류랑 개수 체크
    temp = set()    # 동생 줄 토핑

    for num in topping:
        check[num] -= 1    # 철수 몫에서 토핑 제거
        temp.add(num)    # 동생에게 주기

        if check[num] == 0:    # 철수가 가지고 있던 것 중 모두 동생에게 준 것은 철수 몫에서 제거
            check.pop(num)

        if len(temp) == len(check):    # 동생과 토핑 종류의 수가 같아지면 answer에 추가
            answer += 1
        elif len(temp) > len(check):    # 동생이 많아지는 경우 이후에는 체크할 필요가 없으므로 반복문 빠져나오기
            break

    return answer