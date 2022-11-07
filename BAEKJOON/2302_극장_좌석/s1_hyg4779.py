n = int(input())
m = int(input())


dp = [0]*(n+1)
for _ in range(m):
    dp[int(input())] = 1

# 연속된 좌석수의 가지 수는 피보나치 수열 값
fibo = [0]*41
fibo[0], fibo[1] = 1, 1
for i in range(2, 41):
    fibo[i] = fibo[i-1] + fibo[i-2]

answer = 1
now = 0

for i in range(1, n+1):
    if dp[i] == 0:
        now += 1
    else:
        answer *= fibo[now]
        now = 0

answer *= fibo[now]
print(answer)