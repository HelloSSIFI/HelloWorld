import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def find(p, x):
    if p[x] != x:
        p[x] = find(p, p[x])
    return p[x]


def union(p, a, b):
    a, b = find(p, a), find(p, b)
    if a < b:
        p[b] = a
    else:
        p[a] = b


T = int(input())
for t in range(1, T+1):
    n = int(input())
    arr = [i for i in range(n)]

    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        if find(arr, a) != find(arr, b):
            union(arr, a, b)

    print('Scenario {}:'.format(t))

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if find(arr, a) == find(arr, b):
            print(1)
        else:
            print(0)
    print()