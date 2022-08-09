import math

def solution(enroll, referral, seller, amount):

    parentTree = dict(zip(enroll, referral))
    answer = dict(zip(enroll, [0 for i in range(len(enroll))]))


    for i in range(len(seller)):
        earn = amount[i] * 100
        target = seller[i]

        while True:
            if earn < 10 :
                answer[target] += earn
                break
            else:
                answer[target] += math.ceil(earn * 0.9)
                if parentTree[target] == "-":
                    break
                earn = math.floor(earn*0.1)
                target = parentTree[target]

    return list(answer.values())