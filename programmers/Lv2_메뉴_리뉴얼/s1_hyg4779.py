from collections import defaultdict


def solution(orders, course):
    '''
    실패코드
    '''
    answer = []
    arr = defaultdict(int)

    for i in range(len(orders)):
        pair1 = set(orders[i])                              # 원 비교 문자

        for j in range(i+1, len(orders)):
            pair2 = set(orders[j])                          # 피 비교 문자
            tmp = ''.join(sorted(list(pair1 & pair2)))      # 오름차 순으로 합친 문자

            if len(tmp) in course:arr[tmp]+=1               # 찾는 문자열 길이면 추가가

    list_arr = sorted(arr.keys())

    for x in range(len(arr)):                               # 찾은 조합 속에서 반복되는 조합은 +1
        for y in range(len(arr)):
            if x == y:continue

            if set(list_arr[x]) & set(list_arr[y]) == set(list_arr[x]):
                arr[list_arr[x]] += 1


    for cnt in course:                                      # 길이 별 가장 자주 등장한 조합을 answer에 추가
        q, val = [], 0

        for k, v in arr.items():
            if len(k) != cnt:continue
            q.append((k, v))
            val = max(val, v)

        for el in q:
            if el[1] == val:
                answer.append(el[0])

    return sorted(answer)




print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))