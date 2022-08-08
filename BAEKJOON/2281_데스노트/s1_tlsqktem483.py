import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

inf = sys.maxsize
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
dp = [[inf] * (m+1) for _ in range(n)]


def deathnote(num, rem):
    global dp

    if num >= n:
        return 0
    elif dp[num][rem] != inf:
        return dp[num][rem]
    else:
        # 다음줄
        n_rem = m - arr[num]
        dp[num][rem] = rem * rem + deathnote(num+1, n_rem)

        # 현재줄
        if arr[num] < rem and rem > 0:
            n_rem = rem - arr[num] - 1
            dp[num][rem] = min(dp[num][rem], deathnote(num+1, n_rem))
    return dp[num][rem]


print(deathnote(1, m - arr[0]))