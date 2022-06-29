# 미완료

def make_course(k, menu, orders, temp, i = 0, cnt = 0, best_set=''):
    '''
    k : 원하는 코스 요리 길이
    menu : 단품 메뉴 리스트
    orders: 주문 구성
    i : 단품 메뉴 구성에서 현재의 위치
    temp: 현재 요리 조합
    cnt : 현재 코스 요리 조합의 최대 주문 카운트
    '''
    if len(temp) == k:
        temp_cnt = 0
        for order in orders:
            if set(order) >= set(temp):
                temp_cnt += 1
        if temp_cnt >= 2 and temp_cnt > cnt:
            best_set = temp
            cnt = temp_cnt
            return temp, temp_cnt
        return None

    best_set = ''
    for dish_idx in range(i, len(menu)):
        result = make_course(k, menu, orders, temp + menu[dish_idx], i + 1, cnt)
        if result:
            print('result: ', result)
            temp = result[0]
            cnt = result[1]

    return best_set, cnt


def solution(orders, course):
    answer = []

    single_menu = []
    for order in orders:
        single_menu += list(order)

    # 단품 메뉴 구성
    single_menu = sorted(list(set(single_menu)))

    set_menu = []

    # 세트메뉴 구성
    # 코스 요리 개수 별로 조합 체크
    for c in course:
        result = make_course(c, single_menu, orders, '')
        if result[0]:
            set_menu.append(result[0])

    answer = sorted(set_menu)

    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))

