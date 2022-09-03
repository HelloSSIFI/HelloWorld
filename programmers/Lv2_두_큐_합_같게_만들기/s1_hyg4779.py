def solution(queue1, queue2):

    n, m = sum(queue1), sum(queue2)
    l = len(queue1)

    dp = dict()
    answer = 300000

    def dfs(s1, s2, v1, v2, cnt):
        nonlocal answer

        if s1 == l or s2 == l: return

        if v1 == v2:
            answer = min(answer, cnt)
            return

        if dp.get((s1, s2, v1, v2)) is None:
            dp[(s1, s2, v1, v2)] = True
            dfs(s1+1, s2, v1-queue1[s1], v2+queue1[s1], cnt+1)
            dfs(s1, s2+1, v1+queue2[s2], v2-queue2[s2], cnt+1)

    dfs(0, 0, n, m, 0)

    return answer if answer != 300000 else -1


print(solution([3, 2, 7, 2], [4, 6, 5, 1]))
print(solution([1, 2, 1, 2], [1, 10, 1, 2]))
print(solution([1, 1], [1, 5]))