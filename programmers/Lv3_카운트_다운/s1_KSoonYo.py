
def shoot(cases, target, i=0, cnt=0, score=0, temp=0):
    '''
    cases : 점수 분포
    target : 목표 점수
    i : 시작 인덱스
    cnt: 던진 횟수
    score: 현재 점수
    temp : 싱글과 볼을 합한 횟수
    '''
    global answer
    
    if cnt > answer[0]:                                            # 던진 횟수가 이전에 기록한 최소 횟수보다 크면 
        return                                                     # back

    if score == target:
        if cnt < answer[0]:
            answer = [cnt, temp]
        
        elif temp > answer[1]:
            answer[1] = temp
        return

    if score + 60 * (answer[0] - cnt) < target:                     # 현재 획득 점수에서 이전에 기록한 최소횟수의 나머지 횟수만큼 60점을 던질 때 target을 넘지 못하면
        return                                                      # 더 볼 것도 없으므로 back


    for idx in range(i, len(cases)):
        if score + cases[idx] > target:
            continue
        if cases[idx] <= 20 or cases[idx] == 50:
            shoot(cases, target, idx, cnt + 1, score + cases[idx], temp + 1)
        
        else:
            shoot(cases, target, idx, cnt + 1, score + cases[idx], temp)

def solution(target):
    global answer

    answer = [2000000, 0]       # 최대 얻을 수 있는 점수가 20 * 100,000 이므로 최대 던질 수 있는 횟수는 1점씩 20 * 100,000 만큼 던질 때 횟수

    temp = 0
    while target > 600:
        target -= 300
        temp += 5

    cases_set = set([50])
    for i in range(1, 21):
        for j in range(1, 4):
            cases_set.add(i * j)
    cases = sorted(cases_set, reverse=True)

      
    shoot(cases, target)
    answer[0] += temp
    return answer

print(solution(21))
