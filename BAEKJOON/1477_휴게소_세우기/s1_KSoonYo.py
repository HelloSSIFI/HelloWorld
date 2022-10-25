
# 파라메트릭 서치
# https://www.crocus.co.kr/1000


# N: 현재 휴게소 개수, M: 더 지을 휴게소 개수,  L: 고속도로 길이
N, M, L = map(int, input().split())

rests = [0] + list(map(int, input().split())) + [L]
rests.sort()

left = 1                            # 휴게소 위치 최소
right = L - 1                       # 휴게소 위치 최대(거리 끝에는 휴게소를 세울 수 없음)
minV = 0
while left <= right:
    mid = (left + right) // 2       # 휴게소 거리 간격: mid
    total = 0                       # 새로 지을 수 있는 휴게소 개수
    for i in range(1, N + 2):
        # 현재 휴게소와 이전 휴게소 위치 간격을 휴게소 거리 간격으로 나눠서 추가로 지을 수 있는 휴게소 개수 count
        # 간격에 -1을 하는 이유: 이미 지어진 휴게소의 개수 1은 빼야 하므로
        # ex) mid가 100이고 {200, 400, 501} 위치에 휴게소가 있다면
        # 200 ~ 400 구간의 간격은 200이므로 mid로 나누면 2개가 지어지지만
        # 실제로는 200, 300, 400 으로 이미 지어진 곳의 개수를 빼서 휴게소 1개가 새로 지어질 수 있다.
        total += (rests[i] - rests[i - 1] - 1) // mid

    if total > M:                   # 현재 mid 간격으로 M보다 많이 지을 수 있다면
        left = mid + 1              # 구간의 최대값을 구해야 하므로 거리 간격을 넓혀본다.
    else:                           # 현재 mid 간격으로 M보다 작거나 같게 휴게소를 지을 수 있다면
        right = mid - 1             # 거리 간격을 좁혀본다.(최대 거리 구간의 최소값을 찾아야 하므로)
        minV = mid

print(minV)


