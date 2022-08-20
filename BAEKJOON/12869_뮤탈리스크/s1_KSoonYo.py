import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

N = int(input())
life = list(map(int, input().split()))                  # scv 생명력
visited = []                                            # 방문 체크용

orders = list(permutations([i for i in range(N)]))      # 순서에 따른 순열 
q = deque([(0, life)])                                  # (공격 횟수, 남은 생명력) 
while q:
    attack_cnt, rest_life = q.popleft()
    
    flag = False
    for order in orders:                                # 몇번째 scv를 먼저 공격하는지에 대한 각각의 경우 탐색
        temp = rest_life[:]             
        square = 2                                      # 공격 첫번째는 3^2, 두번째는 3^1, 세번째는 3^0 만큼 데미지 
        for idx in range(N):                            # 순서에 따라 scv 공격
            o = order[idx]                              # order idx 0: 가장 먼저 공격받는 scv, idx 1: 두번째 공격받음, idx 2: 세번째 공격받음
            temp[o] -= 3 ** square
            if temp[o] <= 0:                            # scv 생명력이 0 이하로 떨어지는 경우 0으로 고정
                temp[o] = 0
            square -= 1
        
        if sum(temp) == 0:                              # 현재 공격에서 scv가 모두 파괴된 경우
            flag = True                                 # break
            break
        if temp not in visited:                         # scv 남은 생명력 조합이 이전에 체크한 적이 없다면
            visited.append(temp)                        # 체크(이미 체크했던 생명력 조합은 다시 order를 돌리면서 남은 생명력 계산할 필요가 없음)
            q.append((attack_cnt + 1, temp))            # queue push

    if flag:
        print(attack_cnt + 1)
        break