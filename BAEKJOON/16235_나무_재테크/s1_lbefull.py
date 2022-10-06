import sys
input = sys.stdin.readline


def grow():
    new_wood = [[dict() for i in range(N)] for j in range(N)]           # 새로운 나무 리스트를 반환
    for r in range(N):
        for c in range(N):
            if not wood[r][c]:                                          # 만약 나무가 없는 땅이면
                land[r][c] += A[r][c]                                   # 땅의 양분을 늘려주고(겨울) 다음반복
                continue

            breed = 0                                                   # 현재 위치에서 번식하는 나무 수를 저장
            added = 0                                                   # 죽어서 양분이 된 나무의 양분을 계산하여 저장
            for age, cnt in sorted(wood[r][c].items()):                 # 각각의 나무 나이들을 오름차순으로 순회
                n = land[r][c] // age                                   # 현재 양분으로 현재 나이 나무를 키울 수 있는 최대값을 n으로 저장
                if land[r][c] >= age * cnt:                             # 양분이 현재 나이의 나무 모두를 키울 수 있다면
                    land[r][c] -= age * cnt                             # 양분에서 그 만큼 뺴주고
                    new_wood[r][c][age + 1] = cnt                       # 새로운 나무 리스트에 나이를 1 올려서 저장
                    if not (age + 1) % 5:                               # 만약 새로운 나이가 5의 배수라면
                        breed += cnt                                    # 번식하는 나무 수를 cnt만큼 추가
                elif n:                                                 # 현재 나이의 모든 나무를 성장할 수 없지만 1개 이상 성장할 수 있다면
                    land[r][c] -= age * n                               # n개 만큼 양분을 빼주고
                    new_wood[r][c][age + 1] = n                         # 새로운 나무 리스트에 n개 만큼 저장
                    added += (cnt - n) * (age // 2)                     # cnt - n 만큼 양분으로 변환하여 저장
                    if not (age + 1) % 5:                               # 5의 배수라면
                        breed += N                                      # 번식하는 나무 수에 n 추가
                else:                                                   # 모든 나무가 죽는다면
                    added += cnt * (age // 2)                           # 양분으로 변환하여 저장

            land[r][c] += A[r][c] + added                               # 땅 정보에 고정 양분 A와 추가 양분을 더해줌

            if breed:                                                   # 번식하는 나무가 있다면
                for d in range(8):                                      # 인덱스 범위내의 인접하는 땅에
                    nr = r + dr[d]                                      # 새로운 나무 리스트의 나이 1에 해당하는 값을 breed 만큼 올려줌
                    nc = c + dc[d]
                    if 0 <= nr < N and 0 <= nc < N:
                        new_wood[nr][nc][1] = new_wood[nr][nc].get(1, 0) + breed

    return new_wood                                                     # 새로운 나무 리스트 반환


N, M, K = map(int, input().split())
land = [[5] * N for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]
wood = [[dict() for i in range(N)] for j in range(N)]
for _ in range(M):
    r, c, age = map(int, input().split())
    wood[r - 1][c - 1][age] = 1                             # wood에는 이차원 리스트로 현재 위치를 나타내고 딕셔너리의 key로 나무의 나이, value로 나무 수를 저장

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):                                          # K년 동안 나무 성장 반복
    wood = grow()

answer = 0
for r in range(N):
    for c in range(N):
        for cnt in wood[r][c].values():                     # 모든 나무 수를 더해줌
            answer += cnt
print(answer)
