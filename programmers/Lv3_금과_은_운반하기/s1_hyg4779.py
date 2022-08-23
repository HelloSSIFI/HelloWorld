'''
참고 코드: https://bladejun.tistory.com/166
'''

def solution(a, b, g, s, w, t):
    answer = (10**9) * (10**5) * 4

    start = 0
    # 최악의 경우
    # 걸리는 최소시간(왕복) : 2
    # 금 따로 은 따로(한도시에 금,은만 있을경우) : 2
    # 광물의 최대무게 : 10**9
    # 도시의 최대개수 : 10**5
    end = (10**9) * (10**5) * 4

    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        total = 0

        for i in range(len(g)):
            # 현재 정보
            now_gold = g[i]
            now_silver = s[i]
            now_weight = w[i]
            now_time = t[i]

            # 주어진 시간내에서 이동할 수 있는 횟수(왕복으로 계산)
            move_cnt = mid // (now_time * 2)

            # 편도 추가
            if mid % (now_time * 2) >= now_time:
                move_cnt += 1

            gold += now_gold if (now_gold < move_cnt * now_weight) else move_cnt * now_weight
            silver += now_silver if (now_silver < move_cnt * now_weight) else move_cnt * now_weight
            total += now_gold + now_silver if (now_gold + now_silver < move_cnt * now_weight) else move_cnt * now_weight

        if gold >= a and silver >= b and total >= a + b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1

    return answer