import sys
input = sys.stdin.readline


def finding(p, c):
    if p[c] != c:
        p[c] = finding(p, p[c])
    return p[c]


def union(p, x, y):
    x, y = finding(p, x), finding(p, y)
    if x < y:
        p[y] = x
    else:
        p[x] = y


for tc in range(int(input())):
    # 유저 수
    n = int(input())

    # 서로 연락이 닿을 수 있는 그룹들
    groups = [i for i in range(n)]

    # 그룹 추가
    for _ in range(int(input())):
        a, b = map(int, input().split())
        if finding(groups, a) != finding(groups, b):
            union(groups, a, b)

    print(f'Scenario {tc+1}:')
    # x, y가 같은 그룹인지
    for _ in range(int(input())):
        x, y = map(int, input().split())
        print(0 if finding(groups, x) != finding(groups, y) else 1)
    print()
