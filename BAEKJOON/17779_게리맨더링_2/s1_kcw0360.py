import sys
input = sys.stdin.readline


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]
area_sum = 0
for a in area:
    area_sum += sum(a)
answer = 40000

# 분할하기 위한 i,j 시작점 찾기
for y in range(1, N-1):
    for x in range(0, N-2):

        # 경계의 길이 늘려가며 선거구 범위 안에 존재하는지 확인하기
        for d1 in range(1, N):
            if y - d1 < 0:
                break
            for d2 in range(1, N):
                if y + d2 >= N or x + d1 + d2 >= N:
                    break

                # 각 구역 인구수 합 구하기
                area_list = [0, 0, 0, 0, 0]    # 5번 선거구 idx만 0, 나머지는 idx와 동일
                # 1번 구역
                s = y - 1
                for j in range(x+d1+1):
                    for i in range(s, -1, -1):
                        area_list[1] += area[i][j]
                    if j >= x:
                        s -= 1

                # 2번 구역
                s = y - d1 + d2
                if x+d1+d2 == N-1:
                    s -= 1
                for j in range(N-1, x+d1, -1):
                    for i in range(s, -1, -1):
                        area_list[2] += area[i][j]
                    if j <= x+d1+d2+1:
                        s -= 1

                # 3번 구역
                s = y
                if x == 0:
                    s += 1
                for j in range(x+d2):
                    for i in range(s, N):
                        area_list[3] += area[i][j]
                    if j >= x-1:
                        s += 1

                # 4번 구역
                s = y - d1 + d2 + 1
                for j in range(N-1, x+d2-1, -1):
                    for i in range(s, N):
                        area_list[4] += area[i][j]
                    if j <= x+d1+d2:
                        s += 1

                # 5번 구역
                a14 = sum(area_list)    # 1번 ~ 4번 선거구 인구수 총합
                area_list[0] = area_sum - a14

                # 5개의 선거구 최대 최소 값의 차이를 구한 후, answer과 비교하여 더 작은 값을 answer에 넣어준다
                diff = max(area_list) - min(area_list)
                answer = min(answer, diff)

print(answer)