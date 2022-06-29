from collections import deque


def solution(n, info):

    def dfs(k, s, array):
        nonlocal max_gap

        if k > n: return                                # 어피치 보다 1발 더 쐈다가 가능 화살 수를 넘긴 경우 return

        if k == n:                                      # 화살을 알맞게 쏜 경우
            gap = 0                                     # 점수 차이

            for j in range(11):                         # 10점 부터 계산
                if info[j] + array[j] == 0: continue
                gap += 10-j if info[j] < array[j] else j-10

            if gap > max_gap:                           # 라이언 점수가 어피치 점수보다 큰 경우
                max_gap = gap                           # 최대 점수 값 갱신
                ans.append((gap, array))                # 라이언이 이긴 경우 추가

            return

        new = array[::]                                 # 화살 배열 복사

        for i in range(s, 11):
            tmp = new[i]

            if k + info[i] + 1 <= n:
                new[i] = info[i]+1
                dfs(k+info[i]+1, i+1, new)                  # 어피치 보다 1발 더 쏘고 넘어감
                new[i] = tmp
            dfs(k, i+1, new)                                # 안 쏘고 넘어감

        return

    max_gap, ans = 0, deque([])
    dfs(0, 0, [0]*11)

    if max_gap <= 0:
        return -1

    temp = []

    while ans:
        sum_v, now = ans.popleft()
        if sum_v == max_gap:temp.append(now)



    min_idx, min_v, ans = -1, -1, []
    for arr in temp:
        for idx in range(10, -1, -1):
            if arr[idx]:
                if idx > min_idx or (idx == min_idx and min_v < arr[idx]):
                    min_idx, min_v, ans = idx, arr[idx], arr

    return ans


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))