def solution(priorities, location):
    N = len(priorities)
    answer = 0
    priorities[location] *= -1

    while priorities:
        now = priorities.pop(0)
        N -= 1
        flag = False

        if now < 0:
            now *= -1
            flag = True

        for i in range(N):
            if abs(priorities[i]) > now:
                if flag:
                    now *= -1
                priorities.append(now)
                N += 1
                break
        else:
            answer += 1
            if flag:
                return answer
