import sys
input = sys.stdin.readline
N = int(input())
NUMS = ['2', '3', '5', '7']         # 첫째 자리
ODDS = ['1', '3', '5', '7', '9']    # 둘째 자리 이후


def check(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def dfs(num):
    if len(num) == N:
        print(num)
        return

    for i in ODDS:
        if check(int(num+i)):
            dfs(num+i)


for i in NUMS:
    dfs(i)