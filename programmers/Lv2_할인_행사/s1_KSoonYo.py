def solution(want, number, discount):
    answer = 0
    L = len(discount)
    table = {}
    for i in range(len(want)):
        table[want[i]] = number[i]
        
    for day in range(L - 9):
        sales = discount[day:day + 10]
        for item, want_cnt in table.items():
            sales_cnt = sales.count(item)
            if want_cnt > sales_cnt:
                break
        else:
            answer += 1        
            
    return answer