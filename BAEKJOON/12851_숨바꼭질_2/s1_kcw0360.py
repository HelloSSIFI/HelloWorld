from collections import deque

n, k = map(int, input().split())    # n: 수빈의 시작 위치 , k: 동생 위치

ans_cnt = 0
ans_time = [-1] * 100001
ans_time[n] = 0
q = deque()
q.append(n)


while q:
    temp = q.popleft()

    if temp == k:
        ans_cnt += 1
        continue

    next = [temp-1, temp+1, temp*2]

    for i in next:
        if 0 <= i <= 100000 and (ans_time[i] == ans_time[temp] + 1 or ans_time[i] == -1):
            ans_time[i] = ans_time[temp] + 1
            q.append(i)

print(ans_time[k])
print(ans_cnt)
