from collections import defaultdict

def find(num, rep):
    if num != rep[num]:
        num = find(rep[num])
    return num    

def union(u, v, rep, table):
    rep_u = find(u, rep)
    rep_v = find(v, rep)
    if rep_u != rep_v:    
        rep[rep_v] = rep_u
        table[rep_u] += 1

# 그룹별 대표 박스 번호로 그룹원을 count하고, 그룹원의 수대로 그룹을 내림차순 정렬하여 두 개 그룹을 선정
def solution(cards):
    answer = 0
    table = defaultdict(int)
    rep = [i for i in range(len(cards) + 1)]
    boxes = [False] * (len(cards) + 1)
    
    for idx in range(len(cards)):
        if boxes[idx + 1]:
            continue
        boxes[idx + 1] = True
        
        k = cards[idx]
        table[k] += 1
        while not boxes[k]:
            boxes[k] = True
            union(cards[idx], cards[k-1], rep, table)
            k = cards[k-1]
    
    groups = list(table.values())
    if len(groups) > 1:
        groups.sort(reverse=True)
        answer = groups[0] * groups[1]
    return answer
