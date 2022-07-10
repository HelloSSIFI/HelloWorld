# 1) combinations와 dictionary를 이용한 풀이
# 2) combinations와 Counter를 이용한 풀이
from itertools import combinations
from collections import Counter

# 1)
# def solution(orders, course):
#     answer = []
#     for i in course:
#         course_dict = dict()
#         max_cnt = 0
#         for order in orders:
#             order = sorted(order)
#             results = list(combinations(order, i))
#             for result in results:
#                 if course_dict.get(result):
#                     course_dict[result] += 1
#                 else:
#                     course_dict[result] = 1
#                 max_cnt = max(max_cnt, course_dict[result])

#         for key in course_dict.keys():
#             if max_cnt < 2:
#                 break
#             if course_dict[key] == max_cnt:
#                 answer.append(''.join(key))
#     answer.sort()
#     return answer

# 2)
def solution(orders, course):
    answer = []

    for i in course:
        course_list = []
        for order in orders:
            course_combo = list(combinations(sorted(order), i))             # order 배열 및 문자열에서 i 길이의 조합 리스트 생성
            for course_dish in course_combo:
                course_list.append(''.join(course_dish))

        course_dict = Counter(course_list)                                  # course_list에 있는 요소의 개수를 count하여 dictionary 형태의 Counter 객체 반환
        if not course_dict:
            continue

        max_cnt = max(course_dict.values())
        if max_cnt >= 2:
            for dish, cnt in course_dict.items():
                if cnt == max_cnt:
                    answer.append(dish)

    answer.sort()
    return answer

print(solution(["XYZ", "XWY", "WXA"], [2,3,4]))
