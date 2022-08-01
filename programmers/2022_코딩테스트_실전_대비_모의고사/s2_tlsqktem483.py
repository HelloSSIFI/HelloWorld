def solution(want, number, discount):
    answer = 0
    for day in range(len(discount) - 10 + 1):
        day_discount = discount[day:day+10]
        flag = False
        for i in range(len(want)):
            if day_discount.count(want[i]) < number[i]:
                flag = True
        if not flag:
            answer += 1

    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))