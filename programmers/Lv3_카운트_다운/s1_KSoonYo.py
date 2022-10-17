def shoot(minCnt, cases, target, i=0, shot=0, temp=0):
    global sub
    
    if shot == minCnt:
        if target == 0:
            sub = max(sub, temp)
        return
    for idx in range(i, len(cases)):
        if cases[idx] > target:
            continue
        if cases[idx] == 50 or cases[idx] <= 20:
            shoot(minCnt, cases, target - cases[idx], i, shot + 1, temp + 1)
        else:
            shoot(minCnt, cases, target - cases[idx], i, shot + 1, temp)

def solution(target):
    global sub
    answer = [0, 0]

    cases = set([50])
    for i in range(1, 21):
        cases.add(i)
        cases.add(i * 2)
        cases.add(i * 3)
    cases = list(cases)
    cases.sort(reverse=True)

    # 최대한 적은 다트 -> 목표 점수보다 낮으면서 가장 가까운 점수를 노림
    minCnt = 0
    temp_target = target
    while temp_target:
        if 1 <= temp_target <= 20:
            minCnt += 1
            break
        for case in cases:
            if case > temp_target:
                continue
            minCnt += 1
            temp_target -= case
            break
        
    # minCnt를 넘지 않는 선에서 ball(50) 또는 single을 최대한 많이 맞추기
    
    sub = 0
    shoot(minCnt, cases, target)
    answer = [minCnt, sub]
    return answer

print(solution(58))
