from collections import defaultdict


def solution(k, tangerine):
    answer = 0
    tan_num = defaultdict(int)
    for i in tangerine:    # 종류별 귤 개수 세기
        tan_num[i] += 1

    arr = []
    for t in tan_num:    # 2차원 배열로 만들기 [귤 크기, 수]
        arr.append([t, tan_num[t]])

    arr.sort(key=lambda x: x[1], reverse=True)    # 귤 갯수가 많은 순으로 정렬

    for i in arr:
        answer += 1    # 종류 +1
        k -= i[1]    # 해당 크기의 개수 차감
        if k <= 0:    # 귤을 모두 고른 경우 종료
            return answer