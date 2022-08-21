from collections import defaultdict

def solution(gems):
    answer = []
    gems_length = len(set(gems))
    count_table = defaultdict(int)
    
    gem_set = set()
        
    p1, p2 = 0, 0

    length = 987654321
    while p2 < len(gems):
        gem_set.add(gems[p2])
        count_table[gems[p2]] += 1
        p2 += 1
        while len(gem_set) == gems_length:
            if length > (p2 - p1):
                length = p2 - p1
                answer = [p1 + 1, p2]
        
            count_table[gems[p1]] -= 1
            if count_table[gems[p1]] == 0:
                gem_set.remove(gems[p1])
            p1 += 1
    return answer


# 시간 초과
# 위 코드와 비슷한 로직으로 구현했으나 set 부분집합 여부를 조건문으로 설정하는 것도 시간이 오래 걸리는 듯
# len 길이 여부로 검증해야 효율성 통과
'''

from collections import defaultdict

def solution(gems):
    answer = []
    gems_table = set(gems)
    count_table = defaultdict(int)
    
    gem_set = set()
        

    p1, p2 = 0, 0
    gem_set.add(gems[p1])
    count_table[gems[p1]] += 1

    if gem_set == gems_table:
        return [1, 1]

    length = 987654321
    while p2 < len(gems) and p1 <= p2:
        if gem_set < gems_table:
            p2 += 1
            if p2 < len(gems):
                gem_set.add(gems[p2])
                count_table[gems[p2]] += 1
        else:
            if length > (p2 - p1):
                length = p2 - p1
                answer = [p1 + 1, p2 + 1]
        
            count_table[gems[p1]] -= 1
            if count_table[gems[p1]] == 0:
                gem_set.remove(gems[p1])
            p1 += 1

    return answer
'''

solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])
solution(["AA", "AB", "AC", "AA", "AC"])
solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])
solution(["A", "B" ,"B", "C", "A", "B", "C", "A","B","C"])
solution(["A", "A","A"])
