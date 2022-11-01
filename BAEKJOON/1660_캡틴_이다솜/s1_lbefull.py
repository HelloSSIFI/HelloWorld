def find_min():
    for i in range(1, N + 1):
        temp = N
        for j in tetra:                                     # dp로 현재 대포알 i개를 사면체로 만드는 최소 개수를 구함
            if j > i: break                                 # tetra의 사면체 대포개수를 순회하면서
            if temp > dp[i - j] + 1: temp = dp[i - j] + 1   # 현재 사면체를 추가했을 때 비용과 비교하여 적은것을 선택하여 dp에 넣어줌
        dp.append(temp)


N = int(input())
M = 121
tetra = [1, 4]
for i in range(3, M + 1):                                   # 사면체로 대포알이 완성되는 개수를 30만개까지 구해서
    tetra.append(2 * tetra[i - 2] - tetra[i - 3] + i)       # tetra 리스트에 담아줌

dp = [0]
find_min()
print(dp[N])
