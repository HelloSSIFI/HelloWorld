def solution(arr):
    def comp(sr, sc, n):
        flag = True
        for r in range(sr, sr + n):                 # sr, sc로부터 범위 n을 확인
            for c in range(sc, sc + n):             # 범위 내의 모든 원소가 같을경우 flag는 True
                if arr[sr][sc] != arr[r][c]:        # 아닐경우 False
                    flag = False
                    break
            if not flag:
                break

        if flag:                                    # 모든 원소가 같을 경우
            answer[arr[sr][sc]] += 1                # 해당 원소 개수 + 1
        else:                                       # 원소가 다를 경우
            nn = n // 2                             # 범위를 4개로 나눔
            comp(sr, sc, nn)                        # 해당 범위를 각각 재귀
            comp(sr, sc + nn, nn)
            comp(sr + nn, sc, nn)
            comp(sr + nn, sc + nn, nn)


    answer = [0, 0]
    n = len(arr)
    comp(0, 0, n)
    return answer


# print(solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]]))
