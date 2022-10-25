from collections import Counter


def solution(a):
    """
    빈도수가 많은 수부터 하위로 진행
    O(NL)
    """
    l = len(a)
    if l < 2:
        return 0

    elem = Counter(a)
    answer = -1

    for k in elem.keys():
        if elem[k] <= answer:
            continue

        cnt, idx = 0, 0

        while idx < l-1:
            if (a[idx] != k and a[idx+1] != k) or (a[idx] == a[idx+1]):
                idx += 1
                continue

            cnt += 1
            idx += 2

        answer = max(answer, cnt)

    return answer*2


print(solution([0]))
print(solution([5,2,3,3,5,3]))
print(solution([0,3,3,0,7,2,0,2,2,0]))