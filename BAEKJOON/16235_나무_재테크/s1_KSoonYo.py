import sys
from collections import deque


# 별도 함수 호출 -> 시간 초과
# survived set 이용 -> 시간 초과


# pypy3 통과
input = sys.stdin.readline

N, M, K = map(int, input().split())
lands = [[5] * N for _ in range(N)]                                          # [땅의 양분]
trees_map = [[deque() for _ in range(N)] for _ in range(N)]                  # (r,c) 위치의 나무들 나이
fertilizer = [list(map(int, input().split())) for _ in range(N)]             # 추가할 양분의 양

for _ in range(M):
    tree_r, tree_c, tree_age = map(int, input().split())
    trees_map[tree_r - 1][tree_c - 1].append(tree_age)

dirs = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
while K > 0:
    # survived_trees = spring_summner_fall_winter(N, lands, trees_map, fertilizer, survived_trees)
    
    # 봄, 여름, 가을, 겨울 통합
    for i in range(N):
        for j in range(N):
            fertil = 0
            temp = deque()
            for tree_age in trees_map[i][j]:
                if lands[i][j] >= tree_age:
                    lands[i][j] -= tree_age
                    tree_age += 1
                    temp.append(tree_age)
                else:
                    fertil += (tree_age // 2)
            lands[i][j] += fertil
            trees_map[i][j] = temp

    temp_trees = []
    for r in range(N):
        for c in range(N):
            lands[r][c] += fertilizer[r][c]

            for tree_age in trees_map[r][c]:
                if tree_age % 5 == 0:
                    for d in dirs:
                        nr = r + d[0]
                        nc = c + d[1]
                        if 0 <= nr < N and 0 <= nc < N:
                            temp_trees.append((nr, nc))
    for r, c in temp_trees:
        trees_map[r][c].appendleft(1)
    K -= 1

total = 0
for i in range(N):
    for j in range(N):
        total += len(trees_map[i][j])

print(total)