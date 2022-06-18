# fail -> 시간초과

import sys
from collections import deque
input = sys.stdin.readline

q1 = deque()
q2 = deque()

N, M = map(int, input().split())

for _ in range(M):
    A, B = map(int, input().split())

    q1.append(A)
    q1.append(B)

while q1:
    temp = q1.popleft()
    
    if temp in q1:
        continue
    
    q2.append(temp)


print(*q2)

'''
재만님 풀이(위상정렬 x)


# N, M = map(int, input().split())
# before = [[] for _ in range(N + 1)]         # 인덱스 번호 앞에 서야하는 학생들의 번호를 저장
# after = [[] for _ in range(N + 1)]          # 인덱스 번호 뒤에 서야하는 학생들의 번호를 저장
# result = []
# used = set()
# Q = deque()

# for _ in range(M):
#     a, b = map(int, input().split())        # 입력받은 학생 번호에 맞게 after와 before에 추가
#     before[b].append(a)
#     after[a].append(b)

# for i in range(1, N + 1):                   # 앞에 학생이 없는 학생들의 번호를 Q에 enQ
#     if not before[i]:
#         Q.append(i)

# while Q:                                    # Q가 빌 때 까지 반복
#     cur = Q.popleft()

#     if cur in used:                         # 현재 번호가 이미 used에 있으면 다음반복
#         continue

#     for el in before[cur]:                  # 현재 학생(cur)의 앞에 서야하는 학생번호(el)를 순회
#         if el not in used:                  # el이 아직 줄을 안섰다면 break
#             break

#     else:                                   # cur 앞에서야 하는 학생이 이미 모두 줄을 섰다면
#         result.append(cur)                  # cur을 result와 used에 추가
#         used.add(cur)                       # cur 뒤에 서야하는 학생들을 Q에 enQ

#         for el in after[cur]:
#             Q.append(el)

# print(*result)


'''
