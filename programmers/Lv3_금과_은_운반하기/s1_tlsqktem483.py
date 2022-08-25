"""
이분탐색
O(logN)
"""

def solution(a, b, g, s, w, t):
    answer = float('inf')
    len_city = len(g)

    start, end = 0, (10**9) * (10**5) * 2 * 2

    while start <= end:
        mid = (start + end) // 2
        gold, silver, total = 0, 0, 0

        for i in range(len_city):
            # 왕복으로 다녀올 수 있는 횟수
            cnt = mid // (t[i] * 2)

            # 남은시간에 편도 가능하면 추가
            if mid % (t[i] * 2) >= t[i]:
                cnt += 1

            # 금 운반
            if cnt * w[i] > g[i]:
                gold += g[i]
            else:
                gold += cnt * w[i]

            # 은 운반
            if cnt * w[i] > s[i]:
                silver += s[i]
            else:
                silver += cnt * w[i]

            # 총 운반량 계산
            if cnt * w[i] > g[i] + s[i]:
                total += g[i] + s[i]
            else:
                total += cnt * w[i]

        if gold >= a and silver >= b and total >= a + b:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1

    return answer


print(solution(10, 10, [100], [100], [7], [10]))
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))