"""
N <= 1,000,000
Counter로 초기화 -> O(N) 돌면서 pop
tc 1 : 1,000ms => 4.5ms
"""
from collections import Counter


def solution(topping):
    answer = 0
    t_dict = Counter(topping)
    left = set()

    for t in topping:
        left.add(t)
        t_dict[t] -= 1

        if t_dict[t] == 0:
            t_dict.pop(t)

        if len(t_dict) == len(left):
            answer += 1

    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
print(solution([1, 2, 3, 1, 4]))