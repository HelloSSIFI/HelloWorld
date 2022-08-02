def check():
    for v in memo.values():                 # 모든 제품을 살 수 있는지 체크
        if v > 0:                           # 하나라도 못산다면 False
            return False
    return True


def solution(want, number, discount):
    global memo
    answer = 0
    memo = dict()                           # 각 제품이 몇개씩 필요한지 저장할 딕셔너리
    N = sum(number)

    for i in range(len(want)):              # 제품을 key, 필요한 수를 value로 저장
        memo[want[i]] = number[i]

    for i in range(N):                      # 첫날부터 N일까지 물품을 memo에서 빼줌
        if discount[i] in memo:
            memo[discount[i]] -= 1
    
    if check():                             # 만약 제품을 모두 살 수 있다면 answer +1
        answer += 1
    
    for i in range(N, len(discount)):       # N + 1일부터 마지막날까지 체크
        if discount[i] in memo:             # 할인 범위에 새롭게 추가되는 제품이 memo에 있다면 -1
            memo[discount[i]] -= 1          # 할인 범위에서 없어지는 제품이 memo에 있다면 +1
        if discount[i - N] in memo:         # i번째 날 memo를 갱신 후 모든 제품을 살 수 있다면 answer +1
            memo[discount[i - N]] += 1
        if check():
            answer += 1
    return answer


# print(solution(['banana', 'apple', 'rice', 'pork', 'pot'], [3, 2, 2, 2, 1], ['chicken', 'apple', 'apple', 'banana', 'rice', 'apple', 'pork', 'banana', 'pork', 'rice', 'pot', 'banana', 'apple', 'banana']))
