def solution(N, number):
    '''
    실패코드
    '''
    if N == number:
        return 1

    num_set = {N}

    for cnt in range(2, 9):

        tmp_set = num_set.copy()

        for tmp in tmp_set:
            num_set.add(tmp+N)
            num_set.add(tmp-N)
            num_set.add(tmp*N)

            if tmp:
                num_set.add(tmp//N)

        num_set.add(int(str(N)*cnt))

        if number in num_set:
            return cnt


    else:
        return -1


print(solution(5, 12))