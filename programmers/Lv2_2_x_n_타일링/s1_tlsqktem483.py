"""
dfs : 시간초과
"""
def solution(n):
    answer = 0

    def dfs(remain, arr):
        nonlocal answer

        if remain <= 0:
            answer += 1
            return

        for n in [1, 2]:
            if remain - n >= 0:
                dfs(remain - n, arr + [n])

    dfs(n, [])

    return answer


print(solution(4))