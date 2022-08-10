import sys
from collections import deque

input = sys.stdin.readline


S = int(input())                                    # 목표 이모티콘 개수 
q = deque([(0, 1, 0)])                              # (현재 연산 횟수, 화면에 있는 이모티콘 개수, 클립보드에 있는 이모티콘 개수)
visited = [[0] * (S + 1) for _ in range(S + 1)]         # row: 클립보드 개수, col: 화면 이모티콘 개수, value: 최소 연산 횟수

answer = 0
while q:
    cnt, screen, clip = q.popleft()
    if screen == S:
        answer = cnt
        break

    # 1) 클립보드에 현재 화면에 있는 모든 이모티콘 개수를 저장
    # 2) 클립보드에 있는 이모티콘을 화면에 붙여넣기
    # 3) 화면에 있는 이모티콘 중 하나를 삭제
    case1 = (cnt + 1, screen, screen)
    case2 = (cnt + 1, screen + clip, clip) if clip else ()
    case3 = (cnt + 1, screen - 1, clip) if screen - 1 >= 0 else ()
    for next in [case1, case2, case3]:
        if next and next[1] <= S and not visited[next[1]][next[2]]:
            visited[next[1]][next[2]] = cnt + 1
            q.append(next)

print(answer)