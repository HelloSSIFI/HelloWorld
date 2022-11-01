n = int(input())
T = list(map(int, input().split()))

answer = []
stack = []

for i in range(n):
    # 왼쪽에 검사할 탑들이 있을 때
    while stack:

        # 가까운 순서대로 왼쪽 탑이 현재 탑보다 크면 answer에 추가
        if stack[-1][1] > T[i]:
            answer.append(stack[-1][0]+1)
            break

        # 현재 탑보다 작은 탑이면 pop
        else:
            stack.pop()

    # 검사할 탑이 없다면 0 추가
    if not stack:
        answer.append(0)

    # 현재 탑 인덱스, 크기 append
    stack.append([i, T[i]])

print(*answer)