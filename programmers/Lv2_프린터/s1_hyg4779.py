def solution(priorities, location):
    answer = 0
    priorities[location] *= -1

    while priorities:
        now = priorities.pop(0)
        flag = False

        if now < 0:
            now *= -1
            flag = True

        for tmp in priorities:
            if abs(tmp) > now:
                if flag:
                    now *= -1
                priorities.append(now)
                break
        else:
            answer += 1
            if flag:
                return answer
