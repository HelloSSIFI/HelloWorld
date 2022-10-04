"""
근의공식 풀이
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())


def solve():
    v = (n+2) ** 2 - 4 * k
    if v < 0 or int(v ** 0.5) ** 2 != v:
        print("NO")
        return
    a1, a2 = ((n+2)+v**0.5)/2, ((n+2)-v**0.5)/2
    if float.is_integer(a1) and float.is_integer(a2) and a1 > 0 and a2 > 0:
        print("YES")
    else:
        print("NO")

solve()