from collections import defaultdict


# 완탐 + 조합으로 풀면 시간초과
def combination(table, types, now = 0, temp = []):
    global cnt
    
    for type_idx in range(now, len(types)):
        for cloth in table[types[type_idx]]:
            if cloth not in temp:
                temp.append(cloth)
                cnt += 1
                combination(table, types, now + 1, temp)
                temp.pop()
        
        


# 조합 수학식을 이용하여 풀이해야 통과
# 예를 들어, 머리띠 3개, 안경 1개가 있는 경우
# 선택 가능한 총 경우의 수 = (머리띠를 고르는 경우 3가지 + 머리띠를 착용하지 않는 경우 1가지) * (안경 1개를 고르는 경우 1가지 + 안경을 착용하지 않는 경우 1가지)
# 이때 최소 1개는 입어야 하므로 머리띠와 안경 모두 입지 않는 경우 1가지를 총 경우의 수에서 빼준다.
def solution(clothes):
    global cnt
    answer = 1
    table = defaultdict(int)
    for cloth in clothes:
        table[cloth[1]] += 1
    
    for typ in table.keys():
        answer *= (table[typ] + 1)

    answer -= 1
    
    
    return answer