from collections import defaultdict

def solution(topping):
    answer = 0
    L = len(topping)                          # 토핑 전체 길이
    if L == 1:
        return 0
    
    topping_table = defaultdict(int)          # b가 가지는 토핑의 개수 
    
    a = set()                                 # a가 가지는 토핑 종류
    b = set(topping)                          # b가 가지는 토핑 종류
    
    for i in topping:                         # 테이블 기록
        topping_table[i] += 1
    
    for tp in topping:                        # 토핑을 하나씩 자르면서 a에 토핑 추가 
        if tp in b:                           # 아직 b가 해당 토핑을 보유하고 있다면
            topping_table[tp] -= 1            # b가 가지는 토핑 개수에서 해당 토핑을 -1
            a.add(tp)                         # 해당 토핑을 a가 가지는 토핑 종류에 추가
            
            if topping_table[tp] == 0:        # b에 해당 토핑이 더이상 없다면
                b.remove(tp)                  # b가 가지는 토핑 종류에서 해당 토핑을 제거
        
        if len(a) == len(b):                  # a와 b 토핑 종류 개수가 같다면 
            answer += 1                       # answer + 1
        
        if len(a) > len(b):                   # a가 가지는 토핑 종류 개수가 b를 넘어서는 순간
            break                             # break
    
    return answer