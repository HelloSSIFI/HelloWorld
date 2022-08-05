def solution(beginning, target):
    answer = -1
    n = len(beginning)
    m = len(beginning[0])

    for bit in range(1 << n):
        temp_sum = 0
        temp = [beginning[i][:] for i in range(n)]

        for i in range(n):
            if bit & (1 << i):
                temp_sum += 1
                for j in range(m):
                    if temp[i][j] == 1:
                        temp[i][j] = 0
                    else:
                        temp[i][j] = 1

        for j in range(m):
            temp_column = list(map(list, zip(*temp)))[j][:]
            target_column = list(map(list, zip(*target)))[j][:]
            if temp_column != target_column:
                temp_sum += 1
                for i in range(n):
                    if temp[i][j] == 1:
                        temp[i][j] = 0
                    else:
                        temp[i][j] = 1

        if temp == target:
            if answer == -1:
                answer = temp_sum
            else:
                answer = min(answer, temp_sum)

    return answer


print(solution([[0, 1, 0, 0, 0], [1, 0, 1, 0, 1], [0, 1, 1, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 1, 0]], [[0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]))
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 1], [0, 0, 0], [0, 0, 0]]))