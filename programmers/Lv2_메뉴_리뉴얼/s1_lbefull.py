from itertools import combinations

def solution(orders, course):
    answer = []

    for cnt in course:                                                  # 코스 요리 개수 순회
        order_cnt = dict()                                              # 조합으로 만들어진 메뉴가 몇번 나올지 카운트할 딕셔너리
        max_cnt = 0

        for order in orders:                                            # 각 손님의 주문 순회
            order = "".join(sorted(order))                              # 주문 오름차순 정렬
            for menu in map("".join, combinations(order, cnt)):         # 주문을 코스요리 개수만큼 고른 조합을 순회
                order_cnt[menu] = order_cnt.get(menu, 0) + 1            # 현재 조합을 딕셔너리에서 +1
                if max_cnt < order_cnt[menu]:                           # 딕셔너리의 최대값을 찾아줌
                    max_cnt = order_cnt[menu]
        
        if max_cnt > 1:                                                 # 최대 조합이 2번이상 나왔으면
            for k, v in order_cnt.items():                              # 같은 수의 조합을 모두 찾아서
                if v == max_cnt:                                        # 정답 리스트에 추가
                    answer.append(k)
        
    answer.sort()                                                       # 정답 리스트 오름차순 정렬
    return answer


# print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
