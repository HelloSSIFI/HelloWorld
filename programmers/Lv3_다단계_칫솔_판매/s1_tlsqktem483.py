from collections import defaultdict
from math import trunc


def solution(enroll, referral, seller, amount):
    answer = []
    p = defaultdict(list)

    for i in range(len(enroll)):
        if referral[i] != '-':
            p[enroll[i]].append(referral[i])
        else:
            p[enroll[i]].append('minho')
        p[enroll[i]].append(0)

    for i in range(len(amount)):
        cost = amount[i] * 100
        cur = seller[i]
        ref = p[seller[i]]
        while ref and cost:
            if trunc(cost*0.1) > 0:
                ref_amount = trunc(cost*0.1)
                cur_amount = cost - ref_amount
            else:
                ref_amount = 0
                cur_amount = cost

            p[cur][-1] += cur_amount

            cost = ref_amount
            cur = ref[0]
            ref = p[cur]
    for v in p.values():
        if v:
            answer.append(v[-1])
        else:
            break
    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))