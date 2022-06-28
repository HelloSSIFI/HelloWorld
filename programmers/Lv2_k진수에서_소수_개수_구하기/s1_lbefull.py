def trans(n, k):                                # 정수 n을 입력받아 k진수 문자열 반환
    num = ''
    while n:                                    # n이 0이 아닌동안 반복
        num = str(n % k) + num                  # 나머지를 오른쪾에 추가 후
        n //= k                                 # k로 나눈 몫을 가지고 다시 반복
    return num


def is_prime(n):                                # 소수인지 판별하는 함수
    if n == 1:                                  # 1은 소수가 아니므로 False 리턴
        return False

    for i in range(2, int(n ** 0.5 + 1)):       # n의 제곱근까지만 확인하면 됨
        if not n % i:                           # i로 나누어 떨어지면
            return False                        # 소수가 아니므로 False
    return True                                 # 그 외에는 True


def solution(n, k):
    trans_num = trans(n, k)                     # k진수로 변환
    find_num = []                               # 0 사이에 있거나 왼쪽 혹은 오른쪽 수를 저장할 리스트
    temp = ''                                   # 조건에 맞는 수를 찾을 임시 변수
    for i in range(len(trans_num)):
        if i == 0 and trans_num[i] != '0':      # 맨 왼쪽에 있으면서 0이 아니면
            temp += trans_num[i]                # temp에 추가
        
        elif i == len(trans_num) - 1 and trans_num[i] != '0':
            temp += trans_num[i]                # 맨 오른쪽이면서 0이 아니면
            find_num.append(temp)               # temp에 추가 후 find_num에 추가
        
        elif trans_num[i] == '0':               # 0 이면서
            if temp:                            # temp가 있으면
                find_num.append(temp)           # find_num에 추가 후 temp를 비워줌
                temp = ''

        else:                                   # 그 외의 경우
            temp += trans_num[i]                # temp에 추가
    
    answer = 0
    for num in find_num:                        # find_num에 추가된 숫자 중
        if is_prime(int(num)):                  # 소수가 있으면
            answer += 1                         # 카운트

    return answer


print(solution(110011, 10))
