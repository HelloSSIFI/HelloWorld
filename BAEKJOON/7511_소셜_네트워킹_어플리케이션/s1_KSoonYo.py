import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline


def find(arr, s):
    if s != arr[s]:
        arr[s] = find(arr, arr[s])              # return find(arr, arr[s]) 로 하면 시간초과
    return arr[s]

def union(arr, u, v):
    rep_u = find(arr, u)
    rep_v = find(arr, v)
    if arr[rep_u] != arr[rep_v]:
        arr[rep_v] = arr[rep_u]

for tc in range(int(input())):
    friends = int(input())

    arr = [i for i in range(friends)]

    relations = int(input())
    for r in range(relations):
        u, v = map(int, input().split())
        union(arr, u, v)
    
    print('Scenario ' + str(tc + 1) + ':')
    for m in range(int(input())):
        t1, t2 = map(int, input().split())

        if find(arr, t1) != find(arr, t2):
            print(0)
        else:
            print(1)
    print()