"""
조합 이용한 풀이 => 시간초과
"""
def solution(a):
    answer = 0

    if len(a) < 2:
        return 0

    def comb(arr, n):
        result = []

        if n == 0:
            return [[]]

        for i in range(len(arr)):
            elem = arr[i]
            for c in comb(arr[i+1:], n-1):
                result.append([elem]+c)

        return result

    checked = []
    flag = False
    for l in range(len(a), 1, -1):
        if flag:
            break

        if l % 2:
            continue
        comb_list = comb(a, l)
        if comb_list in checked:
            continue

        checked.append(comb_list)

        for c in comb_list:
            if flag:
                break

            sub_lists = [[c[2*idx-2], c[2*idx-1]] for idx in range(1, l//2+1)]

            inter1 = 0
            inter2 = 0
            for i in range(l//2):
                sub = sub_lists[i]
                if sub[0] == sub[1]:
                    break
                if sub_lists[0][0] in sub:
                    inter1 += 1
                if sub_lists[0][1] in sub:
                    inter2 += 1
            if inter1 == len(sub_lists) or inter2 == len(sub_lists):
                flag = True
                answer = l
                break

    return answer


print(solution([0]))
print(solution([5,2,3,3,5,3]))
print(solution([0,3,3,0,7,2,0,2,2,0]))