from collections import deque
import math

def solution(n, k):
    res = ''

    while n:
        res = str(n%k) + res
        n //= k

    result = deque([])
    idx, s, e, new = 0, 0, 0, False         # index, 문자 시작과 끝, 문자 탐색 여부

    while idx < len(res):

        if not new and res[idx] != '0':
            s, new = idx, True

        elif new and res[idx] == '0':
            e, new = idx, False
            result.append(res[s:e])

        idx += 1

    if new:result.append(res[s:])

    ans = 0

    for tmp in result:

        if int(tmp) < 2:continue

        for num in range(2, int(math.sqrt(int(tmp))+1)):
            if not int(tmp)%num:break
        else:ans +=1

    return ans

print(solution(437674, 3))