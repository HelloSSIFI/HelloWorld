"""
일반 구현 => 효율성테스트 실패
시간복잡도 : O(N*M*K)
"""
def solution(board, skill):
    answer = 0

    for t, r1, c1, r2, c2, power in skill:
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if t == 1:
                    board[i][j] -= power
                else:
                    board[i][j] += power
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] > 0:
                answer += 1
    return answer


print(solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]))
print(solution([[1,2,3],[4,5,6],[7,8,9]], [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]))