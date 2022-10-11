def game_result(apeach, lion):
    apeach_scores = 0
    lion_scores = 0

    for i in range(10):
        if not apeach[i] and not lion[i]:
            continue

        if apeach[i] >= lion[i]:
            apeach_scores += (10 - i)
        else:
            lion_scores += (10 - i)

    if lion_scores > apeach_scores:
        return lion_scores - apeach_scores
    return 0


def shoot(k, i, lion, apeach):
    '''
    k: 남은 화살
    i: 현재 노리는 과녁 타겟
    lion: 라이언의 점수 판
    '''
    global maxV, answer

    if k == 0:
        # 남은 화살이 없으면 return
        result = game_result(apeach, lion)
        if result and maxV < result:
            # 점수차가 최대일 때의 라이언 과녁 상태를 결과값으로 
            maxV = result
            answer = lion[:]
        return
    
    if i == 0:
        lion[i] = k
        shoot(0, -1, lion, apeach)
        lion[i] -= k
        return

    for s in range(k, -1, -1):
        lion[i] = s
        shoot(k - s, i - 1, lion, apeach)
        lion[i] -= s 
    return


def solution(n, info):
    global maxV, answer
    
    answer = []
    maxV = 0

    lion = [0] * 11
    
    # 동일한 상태일 때 점수가 낮은 과녁 순으로 과녁 개수가 많은 것을 정답으로 가지기 때문에 라이언의 화살을 점수가 낮은 과녁에 있는 것부터 체크(시간 절약)
    # 거꾸로 dfs 탐색하면 자연스럽게 점수가 낮은 과녁을 많이 맞추었을 때를 우선 탐색하여 점수 차를 계산하므로 시간 절약 가능
    shoot(n, 10, lion, info)

    if not answer:
        answer = [-1]

    return answer

solution(5, [2,1,1,1,0,0,0,0,0,0,0])
