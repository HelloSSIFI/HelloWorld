def solution(picks, minerals):
    answer = 0
    num = {'diamond': 0, 'iron': 1, 'stone': 2}    # 광물: idx
    fatigue = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]    # 각 곡괭이로 광물을 캘 때의 피로도
    minerals = minerals[:5 * sum(picks)]    # 곡괭이당 5개의 광물을 캐기 때문에 캘 수 있는 해당 개수까지 sling

    check = []    # 5개의 광물을 캤을 때 각 광물의 수  ex) [[다아이몬드 수, 철 수, 돌 수],...]

    idx = 0    # idx
    cnt = 1    # 5개 광물 체크하기 위한 변수
    temp = [0, 0, 0]    # 각 광물당 카운팅
    while idx < len(minerals):
        if cnt > 5:    # 하나의 곡괭이로 캘수 있는 광물을 다 채웠다면 각 변수들 초기화
            check.append(temp)
            cnt = 1
            temp = [0, 0, 0]

        temp[num[minerals[idx]]] += 1    # 광물 카운트
        cnt += 1
        idx += 1

    if sum(temp):    # 마지막으로 카운팅한 것 check에 넣어주기
        check.append(temp)

    # 다이아몬드 철 돌 순으로 피로도가 높기때문에 다이아몬드, 철, 돌이 많은 순으로 정렬한다.
    # 이후 다이아몬드 곡괭이, 철 곡괭이, 돌 곡괭이 순으로 소진하며 체크
    check.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    # 다이아몬드, 철, 돌 순으로 곡괭이를 먼저 소진하기 위에 pick 순서대로 해당 곡괭이 개수만큼 곡괭이 번호 넣는다.
    pick = []
    for i in range(3):
        pick += [i] * picks[i]

    pi = 0    # 사용되는 곡괭이의 idx
    for i in range(len(check)):
        for j in range(3):
            answer += fatigue[pick[pi]][j] * check[i][j]    # 하나의 곡괭이를 소진했을 때 발생하는 피로도 누적
        pi += 1

    return answer