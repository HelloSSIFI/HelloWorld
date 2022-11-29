import sys
input = sys.stdin.readline


N, M = map(int, input().split())
pre = [set() for _ in range(N + 1)]
post = [set() for _ in range(N + 1)]
for _ in range(M):
    K, *temp = map(int, input().split())
    for i in range(K - 1):                          # i번 가수의 이전 순서들을 pre[i]에 담아주고
        for j in range(i + 1, K):                   # 이후의 순서들을 post[i]에 담아줌
            post[temp[i]].add(temp[j])
            pre[temp[j]].add(temp[i])

Q = []
for i in range(1, N + 1):
    if not pre[i]:                                  # 이전 순서가 없는 번호를 Q에 넣어줌
        Q.append(i)

idx = 0
answer = []
while idx < len(Q):
    n = Q[idx]                                      # Q에서 요소를 하나씩 꺼내면서
    idx += 1                                        # 정답에 넣어주고
    answer.append(str(n) + "\n")                    # 자신 이후의 순서들을 변수 pn으로 순회
    for pn in post[n]:                              # pn의 이전 순서 목록에서 자신(n)의 번호를 지워줌
        pre[pn].remove(n)                           # n을 지웠을 때 빈 set이 된다면
        if not pre[pn]:                             # Q에 넣어줌
            Q.append(pn)

if idx < N:                                         # 만약 Q에 모든 번호가 들어가지 않았다면
    answer = ['0']                                  # 순서를 정할 수 없는 경우이므로 0 출력

print(''.join(answer))
