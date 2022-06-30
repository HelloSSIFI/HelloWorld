def rot(r1, c1, r2, c2):
    temp = arr[r1][c1]
    min_num = temp
    for i in range(c1 + 1, c2 + 1):                 # 윗줄 회전
        arr[r1][i], temp = temp, arr[r1][i]
        min_num = min(min_num, temp)

    for i in range(r1 + 1, r2 + 1):                 # 오른쪽 회전
        arr[i][c2], temp = temp, arr[i][c2]
        min_num = min(min_num, temp)

    for i in range(c2 - 1, c1 - 1, -1):             # 아래 회전
        arr[r2][i], temp = temp, arr[r2][i]
        min_num = min(min_num, temp)

    for i in range(r2 - 1, r1 - 1, -1):             # 왼쪽 회전
        arr[i][c1], temp = temp, arr[i][c1]
        min_num = min(min_num, temp)

    return min_num                                  # 최소값 리턴


def solution(rows, columns, queries):
    global answer, arr
    answer = []
    arr = [list(range(i * columns + 1, i * columns + columns + 1)) for i in range(rows)]

    for i in range(len(queries)):                   # 입력받은 쿼리를 인덱스로 사용하기 위해
        for j in range(4):                          # 1씩 값을 줄여줌
            queries[i][j] -= 1
    
    for q in queries:                               # 쿼리를 넣어주고 최소값을 answer에 추가
        answer.append(rot(q[0], q[1], q[2], q[3]))

    return answer


print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
