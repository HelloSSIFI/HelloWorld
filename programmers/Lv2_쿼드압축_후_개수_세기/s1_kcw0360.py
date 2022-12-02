def solution(arr):
    answer = [0, 0]    # [0의 개수, 1의 개수]
    n = len(arr)    # 길이

    def compression(y, x, n):
        start = arr[y][x]
        for i in range(y, y+n):
            for j in range(x, x+n):
                if start != arr[i][j]:    # 다른 값이 나온다면 4등분한 후 각 좌표에서 새롭게 체크(재귀)
                    temp = n // 2
                    compression(y, x, temp)
                    compression(y, x+temp, temp)
                    compression(y+temp, x, temp)
                    compression(y+temp, x+temp, temp)
                    return

        answer[start] += 1

    compression(0, 0, n)
    return answer