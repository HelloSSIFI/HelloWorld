def solution(progresses, speeds):
    answer = []
    rest_progresses = list(map(lambda x : 100 - x, progresses))

    for i in range(len(rest_progresses)):
        if rest_progresses[i] % speeds[i]:
            rest_progresses[i] = rest_progresses[i] // speeds[i] + 1
        else:
            rest_progresses[i] //= speeds[i]

    temp = rest_progresses[0]
    cnt = 1
    for j in range(1, len(rest_progresses)):
        if rest_progresses[j] > temp:
            temp = rest_progresses[j]
            answer.append(cnt)
            cnt = 1
            continue

        cnt += 1

    answer.append(cnt)

    return answer

# queue를 이용해서 푸는 방법도 있다!

