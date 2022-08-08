"""
시간초과
"""
import sys
input = sys.stdin.readline


def check(n):
    if n < 2:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True


N = int(input())

for i in range(int('1'+('0'*(N-1))), int('1'+('0'*N))):
    temp = [str(i)[:j] for j in range(1, N+1)]
    flag = True
    for num in temp:
        if not check(int(num)):
            flag = False
            break
    if flag:
        print(i)
