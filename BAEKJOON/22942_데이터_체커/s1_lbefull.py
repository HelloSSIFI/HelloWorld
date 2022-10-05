import sys
input = sys.stdin.readline


N = int(input())
circle = []
for _ in range(N):
    x, r = map(int, input().split())
    circle.append([x - r, x + r])                               # 원의 x좌표 중 최소값과 최대값을 circle 리스트에 저장
circle.sort()                                                   # circle 리스트를 오름차순 정렬

stack = []
for i in range(N):
    while stack and circle[stack[-1]][1] < circle[i][0]:        # 스택이 있고 스택의 마지막 원의 최대좌표가 현재 원의 최소좌표보다 작으면
        stack.pop()                                             # 스택에서 빼줌

    if not stack:                                               # 스택이 비었다면 현재 원을 넣어주고 다음 반복
        stack.append(i)                                         # 스택의 마지막 원이 현재까지 원들 중 x 최대값이 가장 작은 원이며 현재 원의 최소값보다는 큼
        continue                                                # 현재 원이 스택의 마지막 원과 겹친다면 NO 출력 후 종료

    if circle[stack[-1]][0] == circle[i][0] or circle[i][0] <= circle[stack[-1]][1] <= circle[i][1]:
        print("NO")
        exit()

    stack.append(i)                                             # 겹치지 않는다면 스택에 현재 원을 넣어줌

print("YES")
