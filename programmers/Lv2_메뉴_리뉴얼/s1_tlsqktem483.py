from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    ans = []

    for n in course:
        temp_dict = defaultdict(int)
        max_v = 0
        for o in orders:
            if len(o) >= n:
                for comb in combinations(o, n):
                    temp = ''
                    for c in comb:
                        temp += c
                    temp_dict["".join(sorted(list(temp)))] += 1
        if temp_dict.values():
            max_v = max(temp_dict.values())
        if max_v >= 2:
            for k, v in temp_dict.items():
                if v == max_v:
                    ans.append(k)

    return sorted(ans)


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5]))
print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))