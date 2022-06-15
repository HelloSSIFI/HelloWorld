from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
info = [0] * (N + 1)                        # 해당 인덱스(노드)로 들어오는 간선 수를 저장
graph = [[] for _ in range(N + 1)]          # 해당 인덱스(노드)에 연결된 정점 번호를 저장
result = []
Q = deque()

for _ in range(M):
    a, b = map(int, input().split())        # 두 수(a, b)를 입력받아
    info[b] += 1                            # b는 진입차수를 1증가
    graph[a].append(b)                      # a에는 연결된 간선으로 b를 저장

for i in range(1, N + 1):
    if not info[i]:                         # 진입하는 간선이 없는 경우 Q에 enQ
        Q.append(i)

while Q:
    cur = Q.popleft()                       # Q 에서 deQ

    result.append(cur)                      # 결과에 추가

    for el in graph[cur]:                   # 해당 정점에 연결된 노드를 순회
        info[el] -= 1                       # 진입차수를 1 감소
        if not info[el]:                    # 만약 0이 되었다면
            Q.append(el)                    # Q에 enQ

print(*result)



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
