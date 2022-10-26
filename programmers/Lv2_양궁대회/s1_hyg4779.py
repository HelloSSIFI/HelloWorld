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

            # 라이언이 이겼을 때
            if r > a:
                # 격차가 더 크면 바로 갱신
                if diff < r - a:
                    diff = r - a
                    answer = ryan[:]

                # 격차가 같다면 낮은 점수를 더 많이 쏜 걸로 채택
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