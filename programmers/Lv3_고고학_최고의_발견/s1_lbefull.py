def solution(clockHands):
    def dfs(idx, cnt, arr):
        nonlocal answer
        if idx == N * N:                                                        # 모든 탐색이 끝났다면
            if not arr[-1][-1] and answer > cnt: answer = cnt                   # 마지막 좌표만 12시 방향인지 확인하면 되므로 확인하고
            return                                                              # answer을 최소값으로 갱신 후 리턴

        if cnt > answer: return                                                 # cnt가 answer을 넘어서면 리턴

        r, c = order[idx]
        for t in range(1, 5):                                                   # 총 4번 회전하므로 4번 반복
            arr[r][c] = (arr[r][c] + 1) % 4                                     # 현재 위치와 주변칸을 같이 회전
            for d in range(4):                                                  # 마지막 회전에는 결국 arr이 원래 상태를 유지하므로
                nr = r + dr[d]                                                  # 따로 arr을 복사하지 않음
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < N:                                 # 현재 확인하는 좌표의 위 칸이 존재하면
                    arr[nr][nc] = (arr[nr][nc] + 1) % 4                         # 해당 위치는 이후의 탐색에서 접근할 수 없으므로 12시 방향을 유지해야 함
            if r > 0 and arr[r - 1][c]: continue                                # r이 마지막 행이고 왼쪽에 칸이 존재하면
            if r == N - 1 and c > 0 and arr[r][c - 1]: continue                 # 해당 위치도 이후의 탐색에서 접근할 수 없으므로 12시 방향을 유지해야 함
            dfs(idx + 1, cnt + (t % 4), arr)                                    # 위의 조건을 만족하는 경우에만 재귀


    N = len(clockHands)
    order = []                                                                  # 오른쪽 위에서 왼쪽 아래로 내려가는 대각선 방향으로 탐색
    for i in range(2 * N - 1):                                                  # 순서는 왼쪽 위의 부터 시작하여 해당 대각선 줄이 끝나면 오른쪽 대각선 줄으로 이동하며 탐색
        for j in range(i, -1, -1):                                              # 해당 탐색 순서에 맞게 order에 좌표를 넣어줌
            if 0 <= i - j < N and 0 <= j < N: order.append([i - j, j])

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    answer = N * N * 3
    dfs(0, 0, clockHands)
    return answer


# print(solution([[0, 3, 3, 0], [3, 2, 2, 3], [0, 3, 2, 0], [0, 3, 3, 3]]))
