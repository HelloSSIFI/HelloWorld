def solution(want, number, discount):
    answer = 0

    if len(set(discount) & set(want)) == 0 or set(discount) < set(want):
        return 0

    for day in range(len(discount) - 9):
        items = discount[day : day + 10]
        i = 0
        flag = True
        while i < len(want):
            if items.count(want[i]) >= number[i]:
                i += 1
            else:
                flag = False
                break
        
        if flag:
            answer += 1

    return answer

print(solution())

