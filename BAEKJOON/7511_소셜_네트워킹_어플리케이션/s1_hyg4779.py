import sys
input = sys.stdin.readline

for tc in range(int(input())):
    print(f'Scenario {tc+1}:')

    n = int(input())        # 유저 수

    # 서로 연락이 닿을 수 있는 그룹들
    groups = {}

    # 그룹 추가
    for _ in range(int(input())):
        a, b = map(int, input().split())
        for k, v in groups.items():
            if {a} & groups[k]:
                groups[k].add(b)
                break
            elif {b} & groups[k]:
                groups[k].add(a)
                break
        else:
            groups[a] = {a, b}

    # x, y가 같은 그룹인지
    for _ in range(int(input())):
        x, y = map(int, input().split())
        for k, v in groups.items():
            if groups[k] & {x, y} == {x, y}:
                print(1)
                break
        else:
            print(0)

    print()