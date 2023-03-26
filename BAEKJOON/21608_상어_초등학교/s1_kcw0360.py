import sys
input = sys.stdin.readline

N = int(input())

students = dict()    # 학생의 번호 : [좋아하는 학생의 번호]
for _ in range(N**2):
    temp = list(map(int, input().split()))
    students[temp[0]] = temp[1:]

classroom = [[0]*N for _ in range(N)]    # 교실

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for num in students:
    possible = []    # 현재 학생(num)이 앉을 수 있는 좌석
    for i in range(N):
        for j in range(N):
            if classroom[i][j] != 0:    # 자리가 비어있지 않으면 pass
                continue

            fav = 0    # 인접한 칸에 좋아하는 학생이 있는 수
            emp = 0    # 인접한 칸이 비어있는 수
            for k in range(4):    # 인접한 칸 확인
                y, x = i + dy[k], j + dx[k],
                if 0 <= y < N and 0 <= x < N:    # 교실 좌석 범위 내에 체크
                    if classroom[y][x] in students[num]:    # 좋아하는 학생 목록에 존재하는 경우
                        fav += 1
                    elif classroom[y][x] == 0:    # 비어있는 경우
                        emp += 1
            possible.append([fav, emp, i, j])    # possible에 추가

    possible.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))    # 조건 1,2,3을 만족하는 순서대로 정렬

    classroom[possible[0][2]][possible[0][3]] = num    # 조건을 가장 만족하는 위치에 자리하기

answer = 0
satisfaction = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}    # 인접한 칸에 좋아하는 학생의 수에 따른 만족도
for i in range(N):
    for j in range(N):
        cnt = 0
        for k in range(4):
            y, x = i + dy[k], j + dx[k],
            if 0 <= y < N and 0 <= x < N:
                if classroom[y][x] in students[classroom[i][j]]:
                    cnt += 1    # 인접한 칸에 좋아하는 학생이 존재한다면 카운트

        answer += satisfaction[cnt]    # answer에 만족도 누적

print(answer)