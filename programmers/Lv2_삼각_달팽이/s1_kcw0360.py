def solution(n):
    answer = []
    arr = [[0]*i for i in range(1, n+1)]
    dy, dx = [1, 0, -1], [0, 1, -1]
    d = 0    # 현재 방향
    y, x, num = 0, 0, 1
    end = n * (n+1) // 2    # 최종 값

    while num <= end:
        arr[y][x] = num    # 현 좌표 갱신
        num += 1    # 다음 마킹할 숫자
        ny, nx = y + dy[d], x + dx[d]    # 다음 좌표
        if not (0 <= ny < n and 0 <= nx < n and arr[ny][nx] == 0):    # 좌표를 벗어나거나 마킹이 된 좌표인 경우
            d = (d+1) % 3    # 방향 전환
            ny, nx = y + dy[d], x + dx[d]    # 방향 전환 후 좌표 변경

        y, x = ny, nx    # 좌표 갱신

    for res in arr:    # 정답 양식으로 변경
        answer.extend(res)

    return answer

print(solution(6))