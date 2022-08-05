from collections import defaultdict
import copy

def solution(want, number, discount):
    answer = 0
    buy = defaultdict(int)
    for a, b in zip(want, number):
        buy[a] = b

    for i in range(len(discount)-9):
        check = copy.deepcopy(buy)
        temp = discount[i:i+10]
        flag = True
        for j in temp:
            if check[j]:
                check[j] -= 1
            else:
                flag = False
                break
        if flag:
            answer += 1

    return answer