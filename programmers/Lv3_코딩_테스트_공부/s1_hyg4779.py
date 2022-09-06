from collections import deque


def solution(alp, cop, problems):
    answer = 10000
    n = len(problems)

    max_al, max_cl = max(problems, key=lambda x:x[0])[0], max(problems, key=lambda x:x[1])[1]

    Q = deque([(alp, cop, 0)])
    dp = [[[0]*210 for _ in range(210)] for _ in range(210)]

    while Q:
        al, cl, time = Q.popleft()

        if al >= 210 and cl >= 210:
            answer = min(time, answer)
            continue

        if al > 210 or cl > 210:
            continue

        if dp[al][cl][time]:continue
        dp[al][cl][time] = 1

        for i in range(n):

            need_al, need_cl, prov_al, prov_cl, cost = problems[i]

            if need_al <= al and need_cl <= cl:
                Q.append((al+prov_al, cl+prov_cl, time+cost))

            elif need_al <= al:
                Q.append((al, need_cl, time+abs(need_cl-cl)))

            elif need_cl <= cl:
                Q.append((need_al, cl, time+abs(need_al-al)))

    return answer

print(solution(10, 10, [[10, 15, 2, 1, 2], [20, 20, 3, 3, 4]]))
print(solution(0, 0, [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]))