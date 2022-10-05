"""
배열의 누적합으로 통한 효율성 증대
"""
def solution(board, skill):
    answer = 0
    prefix_sum = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]

    for t, r1, c1, r2, c2, power in skill:
        if t == 1:
            prefix_sum[r1][c1] -= power
            prefix_sum[r1][c2+1] += power
            prefix_sum[r2+1][c1] += power
            prefix_sum[r2+1][c2+1] -= power
        elif t == 2:
            prefix_sum[r1][c1] += power
            prefix_sum[r1][c2 + 1] -= power
            prefix_sum[r2 + 1][c1] -= power
            prefix_sum[r2 + 1][c2 + 1] += power

    for j in range(len(prefix_sum[0])):
        for i in range(1, len(prefix_sum)):
            prefix_sum[i][j] += prefix_sum[i-1][j]

    for i in range(len(prefix_sum)):
        for j in range(1, len(prefix_sum[0])):
            prefix_sum[i][j] += prefix_sum[i][j - 1]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += prefix_sum[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))