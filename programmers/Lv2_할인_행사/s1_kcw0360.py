from collections import defaultdict
import copy


def solution(want, number, discount):
    answer = 0
    buy = defaultdict(int)

    for a, b in zip(want, number):    # 구입 품목: 개수 형태의 dict 생성
        buy[a] = b

    # 10개씩 잘라서 구입 품목 및 개수가 맞는지 확인
    for i in range(len(discount)-9):
        check = copy.deepcopy(buy)    # 구입 품목과 개수가 적인 dict 복사
        temp = discount[i:i+10]    # 10일 구간 나누기
        flag = True

        for j in temp:
            if check[j]:    # 구매 체크
                check[j] -= 1
            else:    # 구입 품목에 없는 품목이 있다면 반복문 중단하기
                flag = False
                break

        if flag:    # 모두 구입이 가능하다면 answer +1
            answer += 1

    return answer