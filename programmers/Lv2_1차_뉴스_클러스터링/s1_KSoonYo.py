def solution(str1, str2):
    answer = 0
    a = str1.upper()
    b = str2.upper()

    # 집합 구하기
    a_set = []
    temp1 = ''
    i = 0
    while i < len(a):
        if a[i].isalpha():
            temp1 += a[i]

            if len(temp1) == 2:
                a_set.append(temp1)
                temp1 = ''
                continue
        else:
            temp1 = ''        
        i += 1
    print('a_set: ', a_set)

    b_set = []
    temp2 = ''
    j = 0
    while j < len(b):
        if b[j].isalpha():
            temp2 += b[j]
            if len(temp2) == 2:
                b_set.append(temp2)
                temp2 = ''
                continue
        else:
            temp2 = ''
        j += 1
    print('b_set:', b_set)

    if len(a_set) == 0 and len(b_set) == 0:
        return 65536

    # 교집합, 합집합 구하기

    inter_set = []
    union_set = []
    temp3 = []
    k = 0
    while True:
        if k >= len(a_set) and k >= len(b_set):
            break
        elif k < len(a_set) and k < len(b_set):
            if a_set[k] not in inter_set:
                inter_set += [a_set[k]] * min(a_set.count(a_set[k]), b_set.count(a_set[k]))
            if a_set[k] not in union_set:
                union_set += [a_set[k]] * max(a_set.count(a_set[k]), b_set.count(a_set[k]))
            if b_set[k] not in union_set:
                union_set += [b_set[k]] * max(a_set.count(b_set[k]), b_set.count(b_set[k]))
        elif k < len(a_set) and k >= len(b_set):
            if a_set[k] not in inter_set:
                inter_set += [a_set[k]] * min(a_set.count(a_set[k]), b_set.count(a_set[k]))
            if a_set[k] not in union_set:
                union_set += [a_set[k]] * max(a_set.count(a_set[k]), b_set.count(a_set[k]))

        elif k >= len(a_set) and k < len(b_set):
            if b_set[k] not in inter_set:
                inter_set += [b_set[k]] * min(a_set.count(b_set[k]), b_set.count(b_set[k]))
            if b_set[k] not in union_set:
                union_set += [b_set[k]] * max(a_set.count(b_set[k]), b_set.count(b_set[k]))
        k += 1
    print('inter_set: ', inter_set)
    print('union_set: ', union_set)

    answer = int(len(inter_set) / len(union_set) * 65536)
    return answer


'''
best solution

import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)



'''

