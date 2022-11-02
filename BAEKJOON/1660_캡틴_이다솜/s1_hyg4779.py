n = int(input())

balls = [0]
b = 0
i = 1
while b < n:
    b += i
    i += 1
    balls.append(b)

print(balls)

dp = [0]*300001
frame = 0
for i in range(len(balls)-1):
    for j in range(balls[i], balls[i]+balls[i+1]+1):
        dp[j] = frame
    frame += 1
print(dp[n])