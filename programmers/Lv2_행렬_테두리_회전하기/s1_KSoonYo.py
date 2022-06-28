# 테두리 범위 구하기, 네 꼭지점
def get_edge(query):
    first_start = (query[0] - 1, query[1] - 1)
    second_start = (query[0] - 1, query[3] - 1)
    third_start = (query[2] - 1, query[3] - 1)
    forth_start = (query[2] - 1, query[1] - 1)

    result = (first_start, second_start, third_start, forth_start)
    return result

# 행렬 회전 후 최소값
def rotate(vertex, matrix):
    
    first, second, third, forth = vertex
    second_value = matrix[second[0]][second[1]]
    third_value = matrix[third[0]][third[1]]
    forth_value = matrix[forth[0]][forth[1]]

    value = set()

    # 위 테두리 한칸씩 옆으로 밀기
    # 거꾸로 순회하여 한칸 뒤 위치로 가져오는 방식
    for y in range(second[1], first[1], -1):
        matrix[first[0]][y] = matrix[first[0]][y - 1]
        value.add(matrix[first[0]][y])
    
    # 오른쪽 테두리 한칸씩 아래로
    for x in range(third[0], second[0], -1):
        matrix[x][second[1]] = matrix[x - 1][second[1]]
        value.add(matrix[x][second[1]])

    matrix[second[0] + 1][second[1]] = second_value
    value.add(second_value)

    # 아래 테두리 한칸씩 옆으로 밀기
    for y in range(forth[1], third[1]):
        matrix[third[0]][y] = matrix[third[0]][y + 1]
        value.add(matrix[third[0]][y])
    
    matrix[third[0]][third[1] - 1] = third_value
    value.add(third_value)

    # 왼쪽 테두리 한칸씩 위로 올리기
    for x in range(first[0], forth[0]):
        matrix[x][forth[1]] = matrix[x + 1][forth[1]]
        value.add(matrix[x][forth[1]])
    
    matrix[forth[0] - 1][forth[1]] = forth_value
    value.add(forth_value)

    return min(value)

def solution(rows, columns, queries):
    answer = []
    
    matrix = []
    num = 1
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(num)
            num += 1
        matrix.append(temp)

    for query in queries:
        result = get_edge(query)
        answer.append(rotate(result, matrix)) 

    return answer

print(solution(6, 6 , [[2,2,5,4], [3,3,6,6], [5,1,6,3]]))
