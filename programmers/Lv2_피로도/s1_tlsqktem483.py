from itertools import permutations


def solution(k, dungeons):
    answer = 0
    per = permutations(dungeons, len(dungeons))

    for p in per:
        hp = k
        cnt = 0
        for d in p:
            if hp >= d[0]:
                hp -= d[1]
                cnt += 1
            else:
                break
        answer = max(answer, cnt)

    return answer


print(solution(80, [[80,20],[50,40],[30,10]]))