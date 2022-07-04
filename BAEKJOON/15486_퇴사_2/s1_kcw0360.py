import sys
input = sys.stdin.readline

n = int(input())

time = []
pay = []
dp = [0] * (n+1)

for _ in range(n):
    a, b = map(int, input().split())
    time.append(a)
    pay.append(b)

temp = 0
for i in range(n):
    temp = max(temp, dp[i])
    if i + time[i] > n:
        continue
    dp[i+time[i]] = max(temp+pay[i], dp[i+time[i]])

print(max(dp))


