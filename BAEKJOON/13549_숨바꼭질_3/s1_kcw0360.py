from collections import deque

n, k = map(int, input().split())    # n: 수빈의 시작 위치 , k: 동생 위치

check = [-1] * 100001
check[n] = 0
q = deque()
q.append(n)


while q:
    temp = q.popleft()

    next = [temp-1, temp+1, temp*2]

    for i in next:
        if 0 <= i <= 100000:
            if i == temp*2:
                if check[i] == -1:
                    check[i] = check[temp]
                    q.appendleft(i)
            else:
                if check[i] == -1:
                    check[i] = check[temp] + 1
                    q.append(i)

print(check[k])
