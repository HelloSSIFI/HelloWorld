import sys
input = sys.stdin.readline

N = int(input())
v = list(map(int, input().split()))
v.sort()
ans = []
min_v = float('inf')

i, j = 0, N-1
while i < j:
    left, right = v[i], v[j]
    s = left + right

    if abs(s) < min_v:
        min_v = abs(s)
        ans = [left, right]

    if s < 0:
        i += 1
    else:
        j -= 1

print(*ans)