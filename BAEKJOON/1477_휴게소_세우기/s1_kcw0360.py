import sys
input = sys.stdin.readline


N, M, L = map(int, input().split())
area = [0] + list(map(int, input().split())) + [L]    # 고속도로의 시작, 휴게소 위치, 고속도로의 끝을 리스트로 생성
area.sort()    # 휴게소 위치에 파악을 위한 정렬
answer = 0
start, end = 1, L
while start <= end:
    mid = (start + end) // 2    # 예상 거리

    cnt = 0    # 휴게소 개수 체크
    # 현재 존재하는 휴게소 끼리 최대거리 찾기
    for i in range(1, len(area)):
        tmp = area[i] - area[i-1]    # 휴게소 사이의 거리
        if tmp > mid:    # mid보다 휴게소 사이의 거리가 큰 경우
            cnt += (tmp-1)//mid    # 휴게소 지을 수 있는 개수를 cnt에 추가

    if cnt > M:    # 휴게소 개수가 예상보다 많은 경우
        start = mid + 1    # mid의 증가를 위해 start를 mid+1 값으로 대
    else:    # 휴게소 개수가 작거나 같은 경우
        end = mid - 1    # mid의 감소를 위해 end 값을 mid-1 값으로 변경
        answer = mid    # 현재의 mid 값이 최댓값의 최솟값이 될 수 있으므로 answer에 저장

print(answer)