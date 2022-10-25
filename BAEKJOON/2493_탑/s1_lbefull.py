N = int(input())
top = list(map(int, input().split()))
stack = []
answer = [0] * N
for i in range(N - 1, -1, -1):                      # 왼쪽으로 신호를 발사하므로 오른쪽부터 탐색
    while stack and stack[-1][0] <= top[i]:         # 이전 신호가 남아있고 현재 탑의 높이가 이전 신호 높이보다 큰 동안 반복
        h, idx = stack.pop()                        # 이전 신호의 인덱스를 찾아
        answer[idx] = i + 1                         # 정답 리스트의 해당 인덱스에 현재 탑의 번호를 저장
    stack.append([top[i], i])

print(*answer)
