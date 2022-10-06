"""
초기 배열을 괄호와 같이 관리, input 도 stdin 써야 시간초과 피함
"""
from sys import stdin
input = stdin.readline
n = int(input())
circles = []
for i in range(n):
    x, r = map(int, input().split())
    circles.append((x - r, i, 0))
    circles.append((x + r, i, 1))

circles.sort()
stack = []
crds = set()
for crd, i, flag in circles:
    if crd in crds:
        print("NO")
        exit(0)
    if flag == 0:
        stack.append((crd, i))
    elif stack[-1][1] != i:
        print("NO")
        exit(0)
    else:
        crds.add(crd)
        stack.pop()
print("YES")