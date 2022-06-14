def solution(numbers, target):
    answer = 0
    
    # dfs 로 현재 수가 +인 상태와 - 인 상태일 때 모두 고려
    def dfs(idx, result, ans = 0):
        '''
        idx: 현재 위치
        result: 결과값
        ans: count 횟수
        '''

        if idx == len(numbers):
            if result == target:
                return 1
            else:
                return 0
        
        now = numbers[idx]
        ans += dfs(idx + 1, result + now)
        ans += dfs(idx + 1, result + (-now))
        
        return ans


    answer = dfs(0, 0)

    return answer

print(solution([4,1,2,1], 4))

