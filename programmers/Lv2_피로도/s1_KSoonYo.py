from itertools import permutations


def solution(k, dungeons):
    answer = -1
    dungeons = list(permutations(dungeons))

    for order in dungeons:
        cnt = 0
        now = k
        for dungeon in order:
            if now >= dungeon[0]:
                cnt += 1
                now -= dungeon[1]
            else:
                break
        answer = max(answer, cnt)

    return answer

