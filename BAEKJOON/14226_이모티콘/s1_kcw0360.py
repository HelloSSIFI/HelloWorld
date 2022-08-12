from collections import deque


S = int(input())

answer = 9876543210
visited = [[0]*(S+1) for _ in range(S+1)]
q = deque()
q.append([1, 0, 0])
visited[1][0] = 1

while q:
    num, cnt, save = q.popleft()

    # 개수가 만들어 지면 반복문 빠져나가기
    if num == S:
        if answer > cnt:
            answer = cnt
            break

    # 화면에 있는 이모티콘을 모두 복사해서 클립보드에 저장
    if num != save and visited[num][num] == 0:
        visited[num][num] = 1
        q.append([num, cnt+1, num])

    # 클립보드에 있는 모든 이모티콘을 화면에 붙여넣기
    if num + save <= S and visited[num+save][save] == 0:
        visited[num+save][save] = 1
        q.append([num+save, cnt+1, save])

    # 화면에 있는 이모티콘 중 하나를 삭제
    if 0 < num and visited[num-1][save] == 0:
        visited[num-1][save]
        q.append([num-1, cnt+1, save])


print(answer)