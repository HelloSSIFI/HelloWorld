# recursion errpr

import sys
input = sys.stdin.readline

def search(idx, temp, target):
    '''
    idx : 현재 코인의 인덱스
    temp : 현재의 수
    target : 목표하는 수
    '''
    global cnt, n
    
    if temp > target:
        return
    
    if temp == target:
        cnt += 1
        return
    
    for coin_idx in range(idx, n):
        search(coin_idx, temp + coins[coin_idx], target)
    


n, k = map(int, input().split())
cnt = 0
coins = []
for _ in range(n):
    coins.append(int(input()))

search(0, 0, k)
print(cnt)
