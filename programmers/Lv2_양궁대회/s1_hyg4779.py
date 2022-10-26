def solution(n, info):
    answer = []
    ryan = [0]*11
    diff = 0

    # m: 쏜 화살 수, idx: 현재 탐색하는 과녁 번호
    def dfs(m, idx):
        nonlocal answer, diff, ryan

        if m == n:
            r, a = 0, 0

            for j in range(11):
                # 둘다 1발은 쐈고,
                # 라이언이 한발이라도 더 쐈다면 라이언 + 아니면 어피치 +
                if ryan[j] > info[j]:
                    r += 10-j
                elif 0 != info[j] and ryan[j] <= info[j]:
                    a += 10-j

            if r > a:
                if diff < r - a:
                    diff = r - a
                    answer = ryan[:]

                elif diff == r - a:
                    for i in range(10, -1, -1):
                        if ryan[i] < answer[i]:
                            break
                        if ryan[i] > answer[i]:
                            answer = ryan[:]
                            break

            return

        for i in range(idx, 11):
            ryan[i] += 1
            dfs(m+1, i)
            ryan[i] -= 1


    dfs(0, 0)

    return answer if answer else [-1]

print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))

'''
def solution(n, info):

    answer = []
    result = 0
    peach = {i: 0 for i in range(11)}

    for i in range(11):
        peach[10-i] = info[i]

    def double_comb(now: dict, idx):
        nonlocal answer, result

        if sum(now.values()) >= n:
            if sum(now.values()) > n:
                return
            r, a = 0, 0

            for j in range(10, -1, -1):
                # 둘다 1발은 쐈고,
                # 라이언이 한발이라도 더 쐈다면 라이언 + 아니면 어피치 +
                if now[j] or peach[j]:
                    if now[j] > peach[j]:
                        r += j
                    else:
                        a += j

            if result <= r-a:

                ryan = [0]*11
                for k, v in now.items():
                    ryan[10-k] = v

                if result < r-a:
                    result = r-a
                    answer = ryan

            return

        for i in range(idx, 0, -1):
            if now[i] <= peach[i]:
                now[i] += 1
                double_comb(now, i)
                now[i] -= 1


    double_comb({i: 0 for i in range(11)}, 10)

    return answer if answer else [-1]

print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))
print(solution(1, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
'''