"""
이분탐색 풀이
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

l, r = 0, n//2
cnt = 0
while l <= r:
    # int 형 자료 범위를 넘어서는 overflow 발생 방지
    m = l + (r-l) // 2
    cnt = (m + 1) * (n - m + 1)

    if cnt < k:
        l = m + 1
    elif cnt > k:
        r = m - 1
    else:
        break
print("YES") if cnt == k else print("NO")