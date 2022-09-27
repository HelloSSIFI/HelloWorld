import sys
input = sys.stdin.readline


def dfs(l):
    global target

    target.append(int(''.join(list(map(str, l)))))
    if target[-1] == 0:
        return

    for i in range(l[-1]-1, -1, -1):
        dfs(l+[i])


N = int(input())
target = []

if N >= 1024:
    print(-1)
else:
    for i in range(10):
        dfs([i])
    print(sorted(target)[N-1])