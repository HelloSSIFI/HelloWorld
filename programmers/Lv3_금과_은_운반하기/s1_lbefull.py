def solution(a, b, g, s, w, t):
    N = len(g)
    l = 0
    r = (max(g) // min(w) + max(s) // min(w) + 2) * max(t) * 2
    while l <= r:                                           # 시간으로 이진 탐색
        m = (l + r) // 2

        gold = 0                                            # 현재 시간에서 운반할 수 있는
        silver = 0                                          # 금과 은과 총량을 저장할 변수
        total = 0
        for i in range(N):
            cnt = (m - t[i]) // (2 * t[i]) + 1              # 시간이 m일 때 i 도시에서 왕복 가능한 횟수

            if g[i] <= cnt * w[i]:                          # 트럭이 금만 운반했을 때 최고량을 gold에 누적
                gold += g[i]
            else:
                gold += cnt * w[i]

            if s[i] <= cnt * w[i]:                          # 트럭이 은만 운반했을 때 최고량을 silver에 누적
                silver += s[i]
            else:
                silver += cnt * w[i]

            if g[i] + s[i] <= cnt * w[i]:                   # 운반한 총량을 total에 누적
                total += g[i] + s[i]
            else:
                total += cnt * w[i]
        
        if gold >= a and silver >= b and total >= a + b:    # 금과 은과 총량 모두 운반 가능하다면
            r = m - 1                                       # m보다 작은 구간에서 반복
        else:                                               # 아니라면 m보다 큰 구간에서 반복
            l = m + 1

    return l


print(solution(10, 10, [100], [100], [7], [10]))
