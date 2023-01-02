def solution(storey):
    def dfs(x, cnt):
        nonlocal answer
        if x == 0:                                      # 0층으로 이동했다면
            if answer > cnt:                            # answer을 최소값으로 갱신
                answer = cnt
            return

        if x == 1:                                      # 아래의 else문은 1을 10으로 만들고 다시 1을 넣어 재귀하여 
            dfs(0, cnt + 1)                             # 무한 반복이 되므로 1의 경우 따로 분리
        else:                                           # 현재 수의 1의 자리를 0으로 만드는 2가지 방법으로 재귀
            dfs(x // 10, cnt + x % 10)                  # 1의 자리 숫자를 빼주는 방법
            dfs(x // 10 + 1, cnt + 10 - x % 10)         # 1의 자리 숫자가 10이 되도록 더해주는 방법


    answer = 200000000
    dfs(storey, 0)
    return answer


# print(solution(2554))
