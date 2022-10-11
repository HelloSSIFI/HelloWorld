results = list(map(int, input().split()))

# 1시작, 41 도착
field = [0 for _ in range(42)]
a, b, c, d = 2, 2, 2, 2
answer = 0

def move(now, i):
    global answer
    if i == 11:
        answer = max(now, answer)
        return

    now = results[i]
    for mal in (a, b, c, d):
        if field[mal+now]:continue

    