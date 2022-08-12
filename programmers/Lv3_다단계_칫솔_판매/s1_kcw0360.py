from collections import defaultdict


def solution(enroll, referral, seller, amount):
    answer = []

    graph = defaultdict(str)
    check = defaultdict(int)
    for i in range(len(referral)):
        check[enroll[i]] = 0
        if referral[i] == '-':
            graph[enroll[i]] = 'minho'
        else:
            graph[enroll[i]] = referral[i]

    for i in range(len(amount)):
        profit = amount[i] * 100
        man = seller[i]

        while profit != 0:
            tmp = profit // 10
            if graph[man] == 'minho':
                check[man] += (profit - tmp)
                break
            else:
                check[man] += (profit - tmp)
                profit = tmp
                man = graph[man]

    for name in enroll:
        answer.append(check[name])

    return answer