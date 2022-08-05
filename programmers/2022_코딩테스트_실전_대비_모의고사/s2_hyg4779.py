from collections import defaultdict


def solution(want, number, discount):
    fruits = defaultdict(int)
    ans = 0
    for w, n in zip(want, number):
        fruits[w] = n

    for f in discount[:10]:
        fruits[f] -= 1

    idx = 0

    for k in want:
        if fruits[k] > 0:break
    else:
        ans += 1

    while idx+10 < len(discount):
        fruits[discount[idx]] += 1
        fruits[discount[idx+10]] -= 1

        idx += 1

        for k in want:
            if fruits[k] > 0:break
        else:
            ans += 1

    return ans