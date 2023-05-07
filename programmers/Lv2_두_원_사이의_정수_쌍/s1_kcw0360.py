import math

def solution(r1, r2):
    answer = 0
    pow_r1 = r1**2    # r1의 제곱값
    pow_r2 = r2**2    # r2의 제곱값

    for i in range(1, r2):    # x축 위의 점은 빼고 계산하기 위해 1부터 시작(y좌표)
        # 반지름이 r2 부채꼴 내에서 y좌표가 i인 지점에서 나올수 있는 점의 수
        answer += math.floor(math.sqrt(pow_r2 - math.pow(r2-i, 2)))

        if i < r1:    # r1 이상은 중첩되는 점이 없기 때문에
            # 반지름이 r1 부채꼴 내에서 y좌표가 i인 지점에서 나올수 있는 점의 수를 차감
            temp = math.sqrt(pow_r1 - math.pow(r1-i, 2))
            answer -= math.floor(temp)

            if temp.is_integer():    # 정수인 경우 원위에 점이 있기 때문에 점의 수 추가
                answer += 1

    answer += (r2 - r1 + 1)    # 축 위에 있는 점의 수 추가

    return answer * 4    # 부채꼴(1/4 형태의 원)만 확인했기 때문에 *4 수행