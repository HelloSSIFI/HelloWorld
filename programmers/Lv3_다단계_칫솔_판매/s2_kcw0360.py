from collections import defaultdict


def solution(enroll, referral, seller, amount):
    money = [0 for _ in range(len(enroll))]
    dict = defaultdict(int)
    for i, e in enumerate(enroll):
        dict[e] = i

    for s, a in zip(seller, amount):
        m = a * 100
        while s != "-" and m > 0:
            idx = dict[s]
            money[idx] += m - m//10
            m //= 10
            s = referral[idx]

    return money