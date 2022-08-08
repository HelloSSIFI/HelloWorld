from itertools import combinations
from collections import defaultdict


def solution(infos, querys):
    answer = []
    info_dict = defaultdict(list)
    for info in infos:
        temp = info.split(" ")
        key = temp[0:-1]
        score = int(temp[-1])

        for i in range(5):
            combi = list(combinations(key, i))
            for c in combi:
                temp_key = ''.join(c)
                info_dict[temp_key].append(score)

    for key in info_dict.keys():
        info_dict[key].sort()

    for query in querys:
        query = query.split(" ")
        query_score = int(query[-1])
        query_key = query[:-1]

        for _ in range(3):
            query_key.remove("and")

        while "-" in query_key:
            query_key.remove("-")
        query_key = ''.join(query_key)

        if query_key in info_dict:
            scoreList = info_dict[query_key]

            if len(scoreList) > 0:
                left, right = 0, len(scoreList)
                while left < right:
                    mid = (left + right) // 2
                    if scoreList[mid] >= query_score:
                        right = mid
                    else:
                        left = mid+1
                answer.append(len(scoreList)-left)
        else:
            answer.append(0)

    return answer




'''
def solution(info, query):
    answer = []

    for q in query:
        q = q.replace('and', '').split()
        cnt = 0

        for i in info:
            i = i.split()
            flag = True

            if int(q[4]) > int(i[4]):
                continue

            for k in range(4):
                if q[k] != i[k] and q[k] != '-':
                    flag = False
                    break

            if flag:
                cnt += 1

        answer.append(cnt)

    return answer
'''