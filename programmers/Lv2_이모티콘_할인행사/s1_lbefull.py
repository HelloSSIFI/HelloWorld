def solution(users, emoticons):
    def dfs(idx):
        if idx == N:                                                        # N개의 이모티콘 할인율이 결정되었다면
            cnt = cost = 0
            for r, c in users:                                              # 유저를 한 명씩 순회하면서
                total = 0                                                   # 유저가 구매하는 이모티콘 가격 총합을 total에 저장
                for i in range(N):
                    if r <= ratio[i]:
                        total += emoticons[i] // 100 * (100 - ratio[i])
                if total >= c:                                              # total이 유저의 기준 금액을 넘어서면
                    cnt += 1                                                # 이모티콘 플러스 유저 +1
                else:                                                       # 아니라면 판매금액 +total
                    cost += total

            if answer[0] < cnt:                                             # 이모티콘 플러스 유저가 많다면
                answer[0] = cnt                                             # 유저와 가격 모두 갱신
                answer[1] = cost
            elif answer[0] == cnt and answer[1] < cost:                     # 플러스 유저는 같으면서 판매 가격이 높다면
                answer[1] = cost                                            # 가격을 갱신
            return

        for r in [10, 20, 30, 40]:                                          # 각 이모티콘들의 할인율을 결정
            ratio[idx] = r                                                  # 할인율을 반복을 통해 정해주고 다음 이모티콘 할인율을 정하러 재귀
            dfs(idx + 1)


    answer = [0, 0]
    N = len(emoticons)
    ratio = [0] * N                                                         # 각 이모티콘 할인 비율을 저장
    dfs(0)
    return answer


# print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
