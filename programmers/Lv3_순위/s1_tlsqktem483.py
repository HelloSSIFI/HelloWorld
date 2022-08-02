from collections import defaultdict


def solution(n, results):
    answer = 0
    winner, loser = defaultdict(set), defaultdict(set)

    for win, lose in results:
        winner[lose].add(win)
        loser[win].add(lose)

    for i in range(1, n+1):
        # i를 이긴 상대는 i에게 진 상대를 이김
        for w in winner[i]:
            loser[w].update(loser[i])
        # i를 진 상대는 i에게 이긴 상대를 짐
        for l in loser[i]:
            winner[l].update(winner[i])

    for i in range(1, n+1):
        if len(winner[i]) + len(loser[i]) == n-1:
            answer += 1
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))