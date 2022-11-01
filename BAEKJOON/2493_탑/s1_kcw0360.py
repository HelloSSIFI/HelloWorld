N = int(input())
tower = list(map(int, input().split()))
stack = []    # 수신 가능한 탑
answer = []
for i in range(N):
    if stack:
        while True:    # 수신 가능한 탑을 찾을 때 까지 반복
            if stack:
                if stack[-1][0] >= tower[i]:    # 수신 가능한 경우
                    answer.append(stack[-1][1]+1)    # 수신 가능한 탑 순서 answer에 저장
                    stack.append([tower[i], i])    # 현재 탑도 수신 가능한 탑 목록에 추가
                    break
                else:    # 수신 불가능한 경우 다음 탑을 확인하기 위해 stack에서 제거
                    stack.pop()
            else:    # 수신 가능한 탑이 하나도 없는 경우
                stack.append([tower[i], i])
                answer.append(0)
                break
    else:    # stack이 비어있는 경우 받을 수 있는 탑이 없으므로 0 & stack에 추가
        stack.append([tower[i], i])
        answer.append(0)

print(*answer)