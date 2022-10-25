import sys

input = sys.stdin.readline

N = int(input())
p = [list(map(int, input().split())) for _ in range(N)]                       # [마을 위치, 인구 수]

p.sort(key=lambda x : x[0])             # 마을 위치 대로 오름차순 정렬

# 실질 거리: 각 사람들까지의 거리
# 위치 거리: 수직선 위치 상 거리

# 첫 마을을 기준으로 총 실질 거리 합과 인구수 합 구하기
total = p[0][1]             # 총 인구 수
distances = 0               # 총 거리
left, right = 0, p[0][1]                       # 우체국의 왼편, 오른편에 있는 인구 수
for i in range(1, N):
    distance = abs(p[i][0] - p[0][0])
    right += p[i][1]
    distances += (distance * p[i][1]) 

minD = distances                         # 최소 실질 거리
pos = p[0][0]                            # 첫 마을 위치
for i in range(1, N):
    # i번째 인덱스 마을에 우체국을 세웠다고 가정
    # 우체국은 한 칸씩 오른쪽으로 이동
    # 오른쪽으로 이동할 때마다 우체국 왼쪽에 위치한 사람 수 만큼 실질 거리가 멀어짐
    # 우체국 오른쪽에 있는 사람들에게는 우체국이 가까워짐
    distance = p[i][0] - p[i - 1][0]     # 이전 마을 과의 위치 거리
    left += p[i - 1][1]                  # 왼편에 이전 마을 인구수를 더해주고
    right -= p[i - 1][1]                 # 오른편에 이전 마을 인구수를 빼준다.
    distances = distances + (left - right) * distance   # 왼쪽 마을 인구 수에서 오른쪽 마을을 뺀 사람 수 만큼의 실질 거리를 기존 실질거리에 더해줌
    if minD > distances:
        minD = distances
        pos = p[i][0]
    elif minD == distance:
        pos = min(pos, p[i][0])
print(pos)


## 시간초과
# S = [0] * (N + 1)
# for k in range(N):
#     # 각 사람들까지의 거리 합 = 두 마을 간 거리 차 x 인구 수
#     # k : 현재 마을 인덱스
#     for h in range(k + 1, N):
#         # h : 목표 마을 인덱스
#         # 거리 차 x 목표 마을 사람 수
#         distance = abs(p[h][0] - p[k][0])
#         S[k] += (distance * p[h][1])
#         S[h] += (distance * p[k][1])

#     # 현재 마을의 계산 결과가 최소값보다 작다면
#     # 현재 마을로 최소 결과값의 인덱스 저장
#     # 이후 최소 결과값의 인덱스로 해당 마을 위치값 추출
#     if minV > S[k]:
#         minP = k
#         minV = S[k]
# print(p[minP][0])
