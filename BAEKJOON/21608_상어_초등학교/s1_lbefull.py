import sys
input = sys.stdin.readline


def calc_pos():
    empty = like_cnt = -1                                           # 주변 빈자리와 좋아하는 학생 수를 초기화
    rr = rc = 0                                                     # 최종적으로 앉게 될 위치 초기화
    for r in range(N):
        for c in range(N):
            if arr[r][c]:                                           # 이미 있는 자리라면 건너뜀
                continue

            nempty = nlike_cnt = 0                                  # 현재 탐색하는 자리의 근처에 빈 자리와 좋아하는 학생수를 저장할 변수
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < N:                     # 교실 범위 안에 있고
                    if arr[nr][nc] == 0:                            # 주변이 빈 자리면 nempty +1
                        nempty += 1

                    elif arr[nr][nc] in likes[s]:                   # 주변이 좋아하는 학생 자리라면 nlike_cnt +1
                        nlike_cnt += 1

            if like_cnt < nlike_cnt:                                # 좋아하는 학생수가 저장된 값보다 크다면
                like_cnt = nlike_cnt                                # 모든 정보를 갱신
                empty = nempty
                rr = r
                rc = c

            elif like_cnt == nlike_cnt and empty < nempty:          # 좋아하는 학생수는 같지만 빈 자리가 많다면
                empty = nempty                                      # 좋아하는 학생수를 제외한 정보 갱신
                rr = r
                rc = c

    arr[rr][rc] = s                                                 # 최종적으로 구해진 자리에 현재 학생 s를 앉힘


def calc_score():                                                   # 점수를 계산하는 함수
    cnt = 0
    for d in range(4):                                              # 현재 좌표 r, c 에서 4방향 탐색해서
        nr = r + dr[d]                                              # 좋아하는 학생 수를 구해서 해당 점수를 리턴
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] in likes[arr[r][c]]:
            cnt += 1

    return scores[cnt]


N = int(input())
arr = [[0] * N for _ in range(N)]
likes = [set() for _ in range(N * N + 1)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for _ in range(N * N):
    s, *like = map(int, input().split())                            # 앉는 학생이 좋아하는 번호를 리스트로 저장
    likes[s].update(like)
    calc_pos()                                                      # 순서대로 앉는 위치를 계산

answer = 0
scores = [0, 1, 10, 100, 1000]
for r in range(N):
    for c in range(N):                                              # 모두 앉았다면 점수를 계산
        answer += calc_score()

print(answer)
