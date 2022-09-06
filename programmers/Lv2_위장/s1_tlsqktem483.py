"""
1차 : Testcase 1 런타임초과
2차 : 각 item 의 개수에 +1 후 중첩곱 => 모든 경우의 수 + 안입은 경우
"""
from collections import defaultdict


def solution(clothes):
    ans = 1
    c = defaultdict(list)

    for cloth, category in clothes:
        c[category].append(cloth)

    for category in c.keys():
        ans *= len(c[category]) + 1
    return ans - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))