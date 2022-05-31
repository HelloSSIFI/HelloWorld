# 테스트케이스 5번에서 런타임에러
# 96 / 100 -> 통과(문자열 길이가 1일 때 조건 처리)

def solution(s):
    original_data = s

    ## 길이가 하나인 경우, 압축할 수 있는 최소 길이는 1 ##
    if len(original_data) == 1:
        return 1

    result_list = []
    max_size = len(original_data) // 2

    def zip_data(size):
        result = ''

        # window 초기 업데이트
        window = ''
        for idx in range(size):
            window += original_data[idx]

        temp = ''
        temp2 = window
        cnt = 1
        for char_idx in range(size, len(original_data)):
            temp += original_data[char_idx]
            if len(temp) == size:
                if temp == window:
                    cnt += 1
                    temp2 = str(cnt) + temp
                    temp = ''
                else:
                    result += temp2
                    window = temp

                    temp = ''
                    temp2 = window
                    cnt = 1
        if temp2:
            result += temp2
        if temp:    
            result += temp 

        return result

    for size in range(1, max_size + 1):
        result_list.append(zip_data(size))

    data_length = list(map(lambda x: len(x), result_list))

    answer = min(data_length)
    return answer

