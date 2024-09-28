def solution(n):
    return find(n, list(), set())


def find(n, now, check):
    if len(now) == n:
        return 1

    cnt = 0
    for i in range(n):
        if i not in check and valid(i, now):
            check.add(i)
            now.append(i)
            cnt += find(n, now, check)
            check.remove(i)
            now.pop()

    return cnt


def valid(num, now):
    idx = len(now)
    for i in range(idx):
        if abs(now[i] - num) == (idx - i):
            return False

    return True
