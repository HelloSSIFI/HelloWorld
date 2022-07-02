def solution(n, info):

    def dfs(k, s, array):                               # 쏜 화살 수, 탐색할 인덱스, 라이언 화살 배열
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
                print(array)

            return


        for i in range(s, 11):
            tmp = array[i]
            if k + info[i] + 1 <= n:
                array[i] = info[i]+1
                dfs(k+info[i]+1, i+1, array[::])                  # 어피치 보다 1발 더 쏘고 넘어감
                array[i] = tmp
            dfs(k, i+1, array)                                # 안 쏘고 넘어감


    max_gap, ans = 0, []
    dfs(0, 0, [0]*11)

    if max_gap <= 0:
        return -1

    temp = []

    while ans:
        sum_v, now = ans.pop()
        if sum_v == max_gap:temp.append(now)

    return temp


print(solution(5, [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]))