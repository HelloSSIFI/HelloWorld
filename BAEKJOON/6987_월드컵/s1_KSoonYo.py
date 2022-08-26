import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline


def check(origin, exp):
    for i in range(len(exp)):
        if origin[i] > exp[i]:
            return False
    return True

teams = [i for i in range(1, 7)]
games = list(combinations(teams, 2))

score_table = []
result_list = []
for _ in range(4):
    visited = []
    scores = list(map(int, input().split()))
    score_table.append(scores)

    result = [0] * 18
    q = deque([([], result)])            # (경기 기록, 경기 결과)
    while q:
        visited, table = q.popleft()

        if len(visited) == len(games):
            result_list.append(table)
            continue

        for game in games:
            if game not in visited:
                visited.append(game)
                team1, team2 = game
                team1_w, team1_d, team1_l = 3 * team1 - 3, 3 * team1 - 2, 3 * team1 - 1
                team2_w, team2_d,  team2_l = 3 * team2 - 3, 3 * team2 - 2,  3 * team2 - 1

                case1 = table[:]
                case2 = table[:]
                case3 = table[:]
                # team1이 이기는 경우
                case1[team1_w] += 1
                case1[team2_l] += 1
                
                # 비기는 경우
                case2[team1_d] += 1
                case2[team2_d] += 1

                # team2가 이기는 경우
                case3[team1_l] += 1
                case3[team2_w] += 1

                if check(case1, scores):
                    q.append((visited[:], case1))
                
                if check(case2, scores):
                    q.append((visited[:], case2))
                
                if check(case3,scores):
                    q.append((visited[:], case3))
                
                break


for score in score_table:
    if score in result_list:
        print('1', end=" ")
    else:
        print("0", end=" ")
