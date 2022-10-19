def solution(cards):
    answer = 0
    cards = [0] + cards
    n = len(cards)

    one_visit = [0]*n

    for idx in range(1, n):
        if one_visit[idx] == 0:
            one = []
            while True:
                if one_visit[idx] == 0:
                    one += [cards[idx]]
                    one_visit[idx] = 1
                    idx = cards[idx]
                else:
                    for jdx in range(2, n):
                        if one_visit[jdx] == 0:
                            two = []
                            while True:
                                if one_visit[jdx] == 0:
                                    two += [cards[jdx]]
                                    one_visit[jdx] = 1
                                    jdx = cards[jdx]
                                else:
                                    answer = max(answer, len(one)*len(two))
                                    break
                    break

    return answer

print(solution([8, 6, 3, 7, 2, 5, 1, 4]))