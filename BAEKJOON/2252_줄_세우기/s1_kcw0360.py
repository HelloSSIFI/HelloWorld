from collections import deque

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]    # graph 생성
check = [0] * (N+1)    # 해당 학생 앞에 반드시 와야할 인원 수 체크

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)    # x번호 학생 뒤에 반드시 와야할 사람 추가
    check[y] += 1    # y번호 앞에 반드시 와야할 인원수 추가

result = []    # 줄 세운 결과 값 순서대로 저장
q = deque()

for i in range(1, N+1):    # check가 0인 사람 deque에 추가 (해당 번호 학생 앞에 반드시 있어야 할 사람이 없는 경우)
    if check[i] == 0:
        q.append(i)

while q:
    temp = q.popleft()
    result.append(temp)    # 줄 세우기
    for i in graph[temp]:    # 뒤에 줄서야하는 사람 체크
        check[i] -= 1    # 뒤에 줄서야 하는 사람 중 반드시 앞에 와야할 사람 인원 -1, temp가 이미 줄을 섰기 때문
        if check[i] == 0:    # 더 이상 앞에 있어야 할 사람이 없다면 줄 서기
            q.append(i)

print(*result)
