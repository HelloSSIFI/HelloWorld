"""
아이디어 : 현재 선택가능한 2개의 원소 중 다음행과의 합이 더 큰 원소를 선택
결과 : Fail
"""
def solution(triangle):
    dp = []
    i = 0
    for n in range(len(triangle)):
        floor = triangle[n]
        if n == 0:
            dp.append(floor[0])
        elif n == len(triangle) - 1:
            dp.append(max(triangle[n][i:i + 2]))
        else:
            comp_1 = floor[i]
            comp_2 = floor[i+1]
            comp_1 += max(triangle[n + 1][i:i + 2])
            comp_2 += max(triangle[n + 1][i + 1:i + 3])
            if comp_2 > comp_1:
                i += 1
            dp.append(floor[i])

    return sum(dp)


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))