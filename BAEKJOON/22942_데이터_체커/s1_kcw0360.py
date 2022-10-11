import sys
input = sys.stdin.readline


N = int(input())

data = []
for i in range(N):
    x, r = map(int, input().split())
    data.append([x-r, i])   # 좌
    data.append([x+r, i])   # 우
data.sort()

stack = []
for i in range(N*2):    # 같은 원의 좌표라면 stack에서 제거, 아니면 stack에 추가
    if stack:
        if stack[-1][1] == data[i][1]:
            stack.pop()
        else:
            stack.append(data[i])
    else:
        stack.append(data[i])

if stack:   # stack이 남은 경우 교점 발생
    print("NO")
else:
    print('YES')