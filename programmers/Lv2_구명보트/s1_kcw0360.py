def solution(people, limit):
    answer = 0
    people.sort()

    # 구명보트는 2명씩 타기 때문에 몸무게가 가장 가벼운 사람, 가장 무거운 사람으로 탐색 시작
    light, heavy = 0, len(people)-1

    while light <= heavy:
        # 몸무게 한도 초과일 경우 무거운 사람 한명, 아닌 경우 에는 무거운 사람 혼자 탑승 한다.
        # 무거운 사람 한명만 탑승하는 경후 heavy의 idx만 -1 이동, 2명 탑승하는 경우에는 light는 +1, heavy는 -1 이동한다.
        if people[light] + people[heavy] <= limit:
            light += 1
        heavy -= 1
        answer += 1

    return answer