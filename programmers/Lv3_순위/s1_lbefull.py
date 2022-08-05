def solution(n, results):
    win = [set() for _ in range(n + 1)]
    lose = [set() for _ in range(n + 1)]
    for a, b in results:
        win[a].add(b)
        lose[b].add(a)
    
    flag = True
    while flag:                                 # n번 선수의 승패 결과에
        flag = False                            # 간접적으로 확인된 순위를 모두 갱신해줌
        for a, b in results:
            if not win[a] >= win[b]:
                flag = True
                win[a].update(win[b])
            if not lose[b] >= lose[a]:
                flag = True
                lose[b].update(lose[a])

    answer = 0
    for i in range(1, n + 1):                       # 승패 합쳐서 n - 1명이 되었다면
        if len(win[i]) + len(lose[i]) == n - 1:     # 등수를 확신할 수 있으므로 answer+1
            answer += 1
    
    return answer


print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
