from itertools import combinations


def dfs(cnt):
    global ans

    if cnt == 15:    # 총 경기 수가 15번이 되었을 때
        for sub in res:
            if sub.count(0) != 3:    # 모든 경기가 치뤄졌음에도 승무패가 0이 되지 않았을 경우
                ans = 0    # ans = 0
                return
        ans = 1
        return

    t1, t2 = games[cnt]    # cnt가 경기 수 이면서 games에서 경기 번호
    check = [(0, 2), (1, 1), (2, 0)]    # 두 팀이 경기하면서 승패, 무무를 체크 하기 위한 idx를 리스트 생성
    for a, b in check:
        if res[t1][a] > 0 and res[t2][b] > 0:    # 둘 다 해당 체크하기 위한 부분들이 남아있을 때
            res[t1][a] -= 1    # 경기 카운트를 하나씩 -1
            res[t2][b] -= 1
            dfs(cnt + 1)
            res[t1][a] += 1    # 재귀 후 다시 복구
            res[t2][b] += 1


answers = []
games = list(combinations(range(6), 2))    # 6개의 팀이 경기 하는 모든 경우의 수
for _ in range(4):
    result = list(map(int, input().split()))    # 결과값 입력받기
    res = [result[i*3:(i+1)*3] for i in range(6)]    # 입력 받은 결과 값을 팀 번호를 idx로 한 2차원 리스트 생성, 해당 팀에 승무패 넣어주기
    ans = 0
    dfs(0)
    answers.append(ans)

print(*answers)