def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key= lambda x: (x[col-1], -x[0]))    # 문제에서 주어진 대로 정렬(조건2)

    for i in range(row_begin-1, row_end):    # 조건4에 나오는 범위에서 XOR 연산
        temp = 0
        for num in data[i]:    # S_i 값 구하기 (조건3)
            temp += num % (i+1)
        answer ^= temp    # XOR 연산

    return answer