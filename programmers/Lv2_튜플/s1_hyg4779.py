def solution(s):

    array = s[2:-2].replace('},{', '|').split('|')


    for i in range(len(array)):
        array[i] = list(map(int, array[i].split(',')))

    # 반환할 리스트
    result = [0]*(len(array))
    # 0번 째 값, 1번째 값, ... (배열 길이 1개, 2개)를 result에 넣어줄 인덱스
    idx = 0

    while idx < len(array):

        for arg in array:
            if len(arg) == idx+1:
                now = arg

                for tmp in now:
                    if not tmp in result:
                        result[idx] = tmp
                        idx += 1
                        break

    return result
