from collections import Counter


def solution(topping):
    answer = 0
    l = set()
    r = Counter(topping)
    for i in range(len(topping)):                       # 토핑을 차례대로 탐색
        l.add(topping[i])                               # l에는 토핑을 추가해주고
        r[topping[i]] -= 1                              # r에서는 토핑을 제거
        if r[topping[i]] == 0: r.pop(topping[i])        # 토핑 종류의 개수가 같다면 answer + 1
        if len(l) == len(r): answer += 1
    return answer
