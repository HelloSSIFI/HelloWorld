def solution(numbers):
    def chk(number, p):                                                 # 트리의 루트가 1개인지 확인하는 함수
        m = len(number) // 2                                            # 문자열의 중간값이 현재 서브트리 문자열의 루트
        if p == 0 and number[m] == '1':                                 # p는 이전 재귀의 루트가 0인지 1인지 정보를 담고있음
            return 0                                                    # 이전 재귀에서 루트가 0인데 현재 루트가 1이라면 만들수 없으므로 0 리턴

        if len(number) == 1:                                            # 리프노드이면서 위 조건을 위 조건에서 리턴을 만나지 않았다면
            return 1                                                    # 가능한 경우이므로 1 반환

        if number[m] == '1':                                            # 루트가 1인 경우
            return chk(number[:m], 1) and chk(number[m + 1:], 1)        # 이전 루트정보를 1을 넣고 중앙을 제거하고 양쪽의 문자열을 각각 재귀하여 and 연산으로 0 또는 1을 리턴

        return chk(number[:m], 0) and chk(number[m + 1:], 0)            # 루트가 0인경우 0을 넣고 위와 마찬가지로 재귀


    answer = []
    for number in numbers:
        number = bin(number)[2:]                                        # 2진수로 변환
        for i in range(1, 7):                                           # 포화 이진 트리의 노드 개수대로 문자열 앞에 0을 추가해줌
            if len(number) <= 2 ** i - 1:
                number = '0' * (2 ** i - 1 - len(number)) + number
                break
        answer.append(chk(number, 1))                                   # chk함수를 실행하여 0 또는 1을 받아 추가
    return answer


# print(solution([42]))
