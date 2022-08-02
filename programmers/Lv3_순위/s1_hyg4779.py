def solution(n, results):
    answer = 0

    win = [set() for _ in range(n+1)]
    lose = [set() for _ in range(n+1)]

    for w, l in results:
        win[w].add(l)
        lose[l].add(w)

    for me in range(1, n+1):

        for idx in win[me]:
            lose[idx].update(lose[me])

        for idx in lose[me]:
            win[idx].update(win[me])

    for person in range(1, n+1):
        if len(win[person]) + len(lose[person]) == n-1:
            answer += 1

    return answer

solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])