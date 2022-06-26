from collections import deque


def solution(n, info):

    def dfs(k, s, array):
        nonlocal max_gap

        if k > n: return                                # 어피치 보다 1발 더 쐈다가 가능 화살 수를 넘긴 경우 return

        if k == n:                                      # 화살을 알맞게 쏜 경우
            gap = 0                                     # 점수 차이

            for j in range(11):                         # 10점 부터 계산
                if info[j] < array[j]:                  # 어피치가 같거나 더 쐈다면
                    gap += 10-j                         # 어피치 점수 +
                else:                                   # 라이언이 더 쐈다면 라이언 점수 +
                    gap -= 10-j

            if gap > max_gap:                           # 라이언 점수가 어피치 점수보다 큰 경우
                max_gap = gap                           # 최대 점수 값 갱신
                ans.append((gap, array))                # 라이언이 이긴 경우 추가

            return

        new = array[::]                                 # 화살 배열 복사

        for i in range(s, 11, 1):
            tmp = new[i]
            val = info[i]

            if not val:                                 # 어피치가 안 쏜 곳 1발만 쏨
                new[i] = 1
                dfs(k+1, i+1, new)
            elif val+k+1 <= n:                          # 어피치보다 1발 더 쏠 때 n발 화살을 초과하지 않으면 쏨
                new[i] = val + 1
                dfs(k+val+1, i+1, new)

            new[i] = tmp
            dfs(k, i+1, new)                            # 안 쏘고 넘어감

        return

    ryan = [0]*11

    max_gap = 0
    ans = deque([])
    dfs(0, 0, ryan)

    if max_gap <= 0:
        return -1

    temp = []

    while ans:
        sum_v, now = ans.popleft()
        if sum_v < max_gap:pass

        if sum_v == max_gap:
            temp.append(now)

    return temp


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))