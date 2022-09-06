def solution(clothes):
    answer = 1
    kinds = dict()
    for name, kind in clothes:                      # 옷 이름은 모두 다르므로 종류별 개수를 딕셔너리에 저장
        kinds[kind] = kinds.get(kind, 0) + 1
    
    for cnt in kinds.values():                      # 현재 종류의 옷을 입지 않은 상태까지 포함하면 cnt+1
        answer *= cnt + 1                           # 모든 상태를 곱하면 모든 경우의 수
    return answer - 1                               # 모든 경우의 수 중 옷을 하나도 입지 않은 경우를 빼줌


# print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
