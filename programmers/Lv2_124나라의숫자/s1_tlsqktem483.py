def solution(n):
    n -= 1
    if n < 3:
        return '124'[n]
    else:
        q, r = divmod(n, 3)
        return solution(q) + '124'[r]