def solution(target):
    answer = []

    # 인덱스: 현재 점수, 값: [쏜 화살의 수, 불 또는 싱글을 쏜 횟수]
    dp = [[target-i, target-i] for i in range(target+1)]

    for i in range(target, -1, -1):
        for j in range(20, 0, -1):

            if i-50 >= 0:
                # 더 적은 화살 수로 갱신
                if dp[i-50][0] > dp[i][0]+1:
                    dp[i-50] = [dp[i][0]+1, dp[i][1]+1]

                # 더 많이 쏜 볼 또는 싱글 수로 갱신
                elif dp[i-50][0] == dp[i][0]+1 and dp[i-50][1] < dp[i][1]+1:
                    dp[i-50] = [dp[i][0]+1, dp[i][1]+1]

            if i-j >= 0:
                # 더 적은 화살 수로 갱신
                if dp[i-j][0] > dp[i][0]+1:
                    dp[i-j] = [dp[i][0]+1, dp[i][1]+1]

                # 더 많이 쏜 볼 또는 싱글 수로 갱신
                elif dp[i-j][0] == dp[i][0]+1 and dp[i-j][1] < dp[i][1]+1:
                    dp[i-j] = [dp[i][0]+1, dp[i][1]+1]

            else:
                break


            if i-2*j >= 0:
                # 더 적게 쏴서 도달할 수 있을 때,
                if dp[i-2*j][0] > dp[i][0]+1:
                    dp[i-2*j] = [dp[i][0]+1, dp[i][1]]

                # 같은 수를 쐇지만, 볼 또는 싱글을 더 많이 맞출때
                elif dp[i-2*j][0] == dp[i][0]+1 and dp[i-2*j][1] < dp[i][1]:
                    dp[i-2*j] = [dp[i][0]+1, dp[i][1]]


            if i-3*j >= 0:
                # 더 적게 쏴서 도달할 수 있을 때,
                if dp[i-3*j][0] > dp[i][0]+1:
                    dp[i-3*j] = [dp[i][0]+1, dp[i][1]]

                # 같은 수를 쐇지만, 볼 또는 싱글을 더 많이 맞출때
                elif dp[i-3*j][0] == dp[i][0]+1 and dp[i-3*j][1] < dp[i][1]:
                    dp[i-3*j] = [dp[i][0]+1, dp[i][1]]


    return dp[0]

print(solution(21))
print(solution(58))

"""
def solution(target):
    shot = target
    ball_n_single = 0

    single = list(range(1, 21))

    def dfs(score, cnt, bs):
        nonlocal shot, ball_n_single

        # answer보다 더 많이 쐈거나 0점 밑으로 내려가면 return
        if cnt > shot or score < 0:
            return

        # 0점이면 볼 또는 싱글 횟수 갱신
        if cnt <= shot and score == 0:
            if cnt == shot:
                ball_n_single = max(bs, ball_n_single)
            else:
                shot = cnt
                ball_n_single = bs

            return


        dfs(score-50, cnt+1, bs+1)

        for s in single:
            if score-s < 0:
                break
            dfs(score-s, cnt+1, bs+1)
            dfs(score-s*2, cnt+1, bs)
            dfs(score-s*3, cnt+1, bs)



    dfs(target, 0, 0)

    return [shot, ball_n_single]
"""