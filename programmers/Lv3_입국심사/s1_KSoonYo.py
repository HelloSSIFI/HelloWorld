
def solution(n, times):
    '''
    n: 심사받아야 하는 사람 수
    times: 심사관들의 심사 시간
    '''
    answer = 0
    time_table = [i for i in range(max(times) * n + 1)]
    
    left = 0
    right = len(time_table) - 1
    while left < right:
        people = 0
        mid = (left + right) // 2

        for time in times:
            people += (mid // time)
        
        if people >= n:
            answer = mid        
            right = mid - 1
        
        else:
            left = mid + 1


    return answer

print(solution(6, [7, 10]))
