from collections import deque
from itertools import permutations


N = int(input())
scv_hp = list(map(int, input().split())) + [0] * (3-N)    # scv 체력을 입력 받을 때 3개가 아니라면 빈자리 채워 무조건 3자리로 만들기
visited = [[[0 for _ in range(61)] for _ in range(61)] for _ in range(61)]    # 거쳐간 체력 체크
atk = list(permutations([9, 3, 1], 3))    # 공격 받는 scv 순서 생성
answer = 0
q = deque()
q.append([scv_hp, 0])    # [scv 체력, 공격 횟수 카운트]

while q:
    hp, cnt = q.popleft()

    flag = True
    for i in range(3):    # scv hp가 모두 0인지 확인
        if hp[i] > 0:    # 0이 아니라면 반복문 빠져나가지 않도록 flag를 False로 변경
            flag = False
    if flag:    # 모두 0이라면 반복문 빠져 나가기
        answer = cnt
        break

    for a in atk:    # 공격 순서 순열을 하나씩 꺼내서 현재 체력에 모두 적용
        tmp = [0, 0, 0]

        for i in range(3):    # 체력이 있는 scv만 데미지 만큼 hp 감소
            if hp[i] - a[i] > 0:
                tmp[i] = hp[i] - a[i]    # 감소된 체력 tmp에 임시 저장

        if not visited[tmp[0]][tmp[1]][tmp[2]]:    # 거처간 체력 조합인지 확인
            visited[tmp[0]][tmp[1]][tmp[2]] = 1    # 거쳐가지 않았다면 방문체크 후 q에 추가
            q.append([tmp, cnt+1])

print(answer)