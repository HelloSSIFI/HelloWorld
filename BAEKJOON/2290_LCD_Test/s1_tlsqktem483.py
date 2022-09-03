"""
Fail 원인 모름
"""
import sys
input = sys.stdin.readline

s, N = input().split()
s = int(s)

ans = [[' ' for _ in range(len(N)*(s+2) + len(N))] for _ in range(2*s + 3)]

start = 0
end = start + s + 2
for n in range(len(N)):
    print(start, end)
    c = N[n]
    # 우
    if c in ['2', '3', '5', '6', '7', '8', '9', '0']:
        ans[0][start+1:end-1] = ['-'] * s
    # 우 상
    if c in ['1', '2', '3', '4', '7', '8', '9', '0']:
        for i in range(1, 1 + s):
            ans[i][end-1] = '|'
    # 우 하
    if c in ['1', '3', '4', '5', '6', '7', '8', '9', '0']:
        for i in range(s + 2, 2*s + 2):
            ans[i][end - 1] = '|'
    # 중
    if c in ['2', '3', '4', '5', '6', '8', '9']:
        ans[s + 1][start + 1:end - 1] = ['-'] * s
    # 좌 상
    if c in ['4', '5', '6', '8', '9', '0']:
        for i in range(1, 1 + s):
            ans[i][start] = '|'
    # 좌 하
    if c in ['2', '6', '8', '0']:
        for i in range(s + 2, 2 * s + 2):
            ans[i][start] = '|'
    # 하
    if c in ['2', '3', '5', '6', '8', '9', '0']:
        ans[-1][start + 1:end - 1] = ['-'] * s
    start = end + 1
    end = start + s + 2

for i in range(2*s + 3):
    print(*ans[i])