from collections import defaultdict, deque
import sys
input = sys.stdin.readline

T = int(input())    # T: 테스트 케이스의 개수
answer = []
for _ in range(T):
    N, K = map(int, input().split())    # N: 건물의 개수 , K: 건물간의 건설순서 규칙의 총 개수
    build_time = [0] + list(map(int, input().split()))    # 각 건물 짓는시간
    buildings = defaultdict(list)    # 건물간 규칙 관계도
    check = [0] * (N+1)    # 먼저 지어져야하는 건물이 있는 건물인지 체크
    for _ in range(K):
        a, b = map(int, input().split())
        buildings[a].append(b)
        check[b] += 1
    win = int(input())    # 승리하기 위해 건설해야할 건물 번호
    dp = [0] * (N + 1)

    q = deque()
    for i in range(1, N+1):
        if check[i] == 0:    # 선행 건물이 없는 경우 q에 추가 및 dp에 해당 시간 저장
            q.append(i)
            dp[i] = build_time[i]

    while q:
        now = q.popleft()
        for i in buildings[now]:
            check[i] -= 1
            dp[i] = max(dp[i], build_time[i] + dp[now])    # 건설 시간이 오래 걸리는 것으로 저장

            if check[i] == 0:    # 선행 건물이 모두 완료 된 후 다음 건물 짓기 진행
                q.append(i)
        if check[win] == 0:
            break

    answer.append('{}\n'.format(dp[win]))

print(''.join(answer))

