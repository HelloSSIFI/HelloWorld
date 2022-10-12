def solution(numbers):
    answer = []

    for num in numbers:
        if num % 2:    # 홀수인 경우
            # bin => 2진수로 바꿔주는 내장함수
            bin_num = list('0' + bin(num)[2:])
            idx = ''.join(bin_num).rfind('0')
            bin_num[idx] = '1'
            bin_num[idx+1] = '0'

            # int(숫자, 2) 2진수를 10진수로 변환
            answer.append(int(''.join(bin_num), 2))

        else:    # 짝수인 경우 +1 해서 answer에 추가
            answer.append(num+1)

    return answer