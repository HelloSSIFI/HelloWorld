import math


def solution(n, l, r):

    # 5**n 범위에 대한 1의 개수: 4**n
    # 프렉탈: 삼각형 대칭 구조

    def sol(x):
        if x <= 2: return x
        elif x <= 5: return x-1

        # x가 5의 몇제곱 수인지 판별
        base = int(math.log(x)/math.log(5))
        d, r = divmod(x, 5**base)

        ans = d * (4**base)

        if d == 2: return ans
        elif d >= 3: ans -= 4**base

        return ans + sol(r)

    return sol(r) - sol(l-1)