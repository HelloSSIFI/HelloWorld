from collections import deque


def bfs(n, p):

    l = [0] * 11
    answer = []
    max_val = 0
    q = deque([(0, n, l)])

    while q:
        (i, r, arr) = q.popleft()
        # 잔여 화살 없을 시 점수 계산
        if r == 0:
            lion = 0
            apeach = 0
            for scr in range(len(arr)):
                if arr[scr] > p[scr]:
                    lion += 10 - scr
                elif p[scr]:
                    apeach += 10 - scr

            if lion > apeach:
                gap = lion - apeach
                if gap > max_val:
                    max_val = lion - apeach
                    answer.clear()
                if gap < max_val:
                    continue
                answer.append(arr)
        elif r < 0:
            continue

        elif i == 10:
            temp = arr[::]
            temp[i] = n - sum(temp)
            q.append((-1, 0, temp))

        if i < len(arr) and r > 0:
            shoot = [p[i] + 1, 0]

            for s in shoot:
                temp = arr[::]
                temp[i] = s
                q.append((i + 1, r - s, temp))

    return answer


def solution(n, p):
    ans = bfs(n, p)

    if not ans:
        return [-1]
    elif len(ans) == 1:
        return ans[0]
    else:
        return ans[-1]


print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))
print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))