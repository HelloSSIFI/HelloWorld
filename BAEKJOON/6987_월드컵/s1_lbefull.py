def dfs(cnt, idx):                      # 경기를 치르는 팀을 고르는 함수
    if cnt == 2:
        games.append(game[:])
        return
    
    for i in range(idx, 6):
        game.append(i)
        dfs(cnt + 1, i + 1)
        game.pop()


def match(cnt):                         # 각 경기당 승무패를 추가하면서 경우의 수를 찾는 함수
    global ans
    if cnt == 15:                       # 15 경기가 모두 채워졌으면
        if result == arr:               # 주어진 arr과 같은지 판별하여
            ans = 1                     # 같으면 ans를 1로 만들어줌
        return

    if cnt > 4:                         # 가지치기
        if result[:3] != arr[:3]:       # 5경기가 끝났을 경우 첫번째 팀은 모든 경기가 끝났으므로
            return                      # 앞의 3개의 숫자가 경우의수와 같아야 함
    if cnt > 8:                         # 마찬가지로 9경기가 끝나면 두번째 팀의 모든 경기가 끝남
        if result[:6] != arr[:6]:
            return
    if cnt > 11:
        if result[:9] != arr[:9]:
            return
    a, b = games[cnt]
    for i in range(3):                  # 15 경기를 모두 진행하지 않았다면
        result[3 * a + i] += 1          # 각 경기당 승무패의 경우를 기록하고 재귀
        result[3 * b + 2 - i] += 1
        match(cnt + 1)
        result[3 * a + i] -= 1
        result[3 * b + 2 - i] -= 1


games = []
game = []
result = [0] * 18
answer = []
dfs(0, 0)

for _ in range(4):
    ans = 0
    arr = list(map(int, input().split()))
    match(0)
    answer.append(ans)

print(*answer)
