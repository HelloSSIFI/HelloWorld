def solution(n, results):
    answer = 0
    win_table = [set() for _ in range(n + 1)]           # i번째 복서가 이긴 상대 기록용 테이블
    lose_table = [set() for _ in range(n + 1)]          # i번째 복서가 진 상대 기록용 테이블

    for result in results:
        winner, loser = result[0], result[1]
        win_table[winner].add(loser)                    # 그래프 입력받고 테이블 기록
        lose_table[loser].add(winner)
    
    for i in range(1, n + 1):
        for to_win in win_table[i]:                        # i번째 복서가 이긴 상대 to_win은
            lose_table[to_win].update(lose_table[i])       # i번째 복서가 진 모든 상대에게 진다.

        for by_lose in lose_table[i]:                      # i번째 복서가 진 상대 by_lose는
            win_table[by_lose].update(win_table[i])        # i번째 복서가 이긴 모든 상대를 이긴다.

    for k in range(1, n + 1):
        if len(win_table[k]) + len(lose_table[k]) == n - 1:
            answer += 1

    return answer

# solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
solution(4, [[4, 1], [4, 2], [4, 3]])
