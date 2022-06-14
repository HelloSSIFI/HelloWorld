def solution(N, number):
    '''
    정답코드
    '''
    if N == number:
        return 1

    num_set_list = []

    for cnt in range(1, 9):                     # 1개부터 8개까지 확인

        num_set = set()
        num_set.add(int(str(N)*cnt))            # N을 이어 붙여 만든 케이스
        for i in range(cnt - 1):
            for op1 in num_set_list[i]:
                for op2 in num_set_list[-i-1]:

                    num_set.add(op1 + op2)
                    num_set.add(op1 - op2)
                    num_set.add(op1 * op2)
                    if op2 != 0:
                        num_set.add(op1/op2)

        if number in num_set:
            return cnt

        num_set_list.append(num_set)

    else:
        return -1


print(solution(5, 12))