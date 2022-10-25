import math, sys
input = sys.stdin.readline


N = int(input())
town = []    # 마을 정보
population = 0    # 총 인구수
for _ in range(N):
    town.append(list(map(int, input().split())))    # [마을 위치, 인구수]
    population += town[-1][1]    # 마을 인구수 더하기
town.sort()    # 마을 위치 순으로 정렬

check = 0    # 누적 체크
mid = math.ceil(population/2)    # 총 인구수 절반(소수점이 존재하면 올림)
answer = 0    # 우체국 위치
for t, p in town:
    check += p    # 인구수 누적
    if check >= mid:    # 누적 인구수가 mid값 이상이 되기 시작하는 마을이 우체국을 세울 장소
        answer = t
        break

print(answer)