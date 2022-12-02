def solution(n):
    arr = [[0] * i for i in range(1, n + 1)]
    dr = [1, 0, -1]                                     # 숫자가 증가하는 칸대로 탐색하여 채워넣음
    dc = [0, 1, -1]                                     # 삼각형대로 방향을 전환하도록 dr, dc를 만들어줌
    cnt = c = d = 0
    r = -1
    while cnt < n * (n + 1) // 2:                       # 삼각형의 범위를 벗어나거나 이미 채운칸이면
        cnt += 1                                        # 방향을 바꿔줌
        if r + dr[d] < 0 or n <= r + dr[d] or c + dc[d] < 0 or len(arr[r + dr[d]]) <= c + dc[d] or arr[r + dr[d]][c + dc[d]] != 0:
            d = (d + 1) % 3
        r += dr[d]
        c += dc[d]
        arr[r][c] = cnt

    answer = []
    for el in arr:                                      # 2차원 배열을 1차원으로 합쳐줌
        answer.extend(el)

    return answer 


# print(solution(4))
