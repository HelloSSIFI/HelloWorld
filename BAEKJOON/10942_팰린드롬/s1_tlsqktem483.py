"""
완전탐색
시간초과
"""
import sys
from collections import deque
input = sys.stdin.readline


def ispalindrome(n):
    number = deque(n[:])
    while number:
        if len(number) == 1:
            return True
        l, r = number.popleft(), number.pop()

        if l != r:
            return False
    return True


ans = []
N = int(input())
board = list(map(int, input().split()))
M = int(input())

for _ in range(M):
    S, E = map(int, input().split())

    if ispalindrome(board[S-1:E]):
        print(1)
    else:
        print(0)


