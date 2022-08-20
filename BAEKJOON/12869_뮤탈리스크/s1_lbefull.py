from collections import deque


N = int(input())
scv = list(map(int, input().split()))
while len(scv) < 3:                                                                 # scv를 3기로 맞춰줌
    scv.append(0)
q = deque()
q.append([scv[0], scv[1], scv[2], 0, 0])                                            # q에 초기 체력과 인덱스, 횟수를 넣어줌
num = [9, 3, 1]                                                                     # 각각 데미지를 리스트로 표현
permu = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]          # 한 번 공격에 나올 수 있는 순열

while q:                                                                            # q가 빌 때까지 반복
    s1, s2, s3, idx, cnt = q.popleft()
    
    if s1 <= 0 and s2 <= 0 and s3 <= 0:                                             # 모든 scv가 죽으면 반복종료
        break                                                                       # 아니라면 중복을 없애기 위해 이전에 가장 마지막 인덱스였던 부분부터 순열을 돌면서

    for i in range(idx, 6):                                                         # 깎인 체력을 계산하고 현재 가장 마지막 인덱스와 cnt + 1을 q에 넣어줌
        q.append((s1 - num[permu[i][0]], s2 - num[permu[i][1]], s3 - num[permu[i][2]], i, cnt + 1))

print(cnt)
