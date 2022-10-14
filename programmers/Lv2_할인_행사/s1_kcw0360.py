# 2022 코딩테스트 실전 대비 모의고사 2번과 같은 문제(더 빠른 풀이)
from collections import defaultdict


def solution(want, number, discount):
    answer = 0
    buy = defaultdict(int)
    for idx, val in enumerate(want):
        buy[val] = idx

    for i in range(len(discount)-9):
        temp = [0] * len(number)
        flag = True

        for j in range(i, i+10):
            if discount[j] in buy:
                temp[buy[discount[j]]] += 1
            else:
                flag = False
                break

        if flag:
            if temp == number:
                answer += 1

    return answer