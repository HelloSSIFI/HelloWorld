def solution(cards):
    cards = [0] + cards
    check = []

    for i in range(1, len(cards)):
        if cards[i] == 0:
            continue

        res = 0
        idx = i
        while cards[idx] != 0:
            res += 1
            tmp = idx
            idx = cards[idx]
            cards[tmp] = 0

        check.append(res)

    check.sort()

    if len(check) >= 2:
        return check[-1] * check[-2]
    else:
        return 0