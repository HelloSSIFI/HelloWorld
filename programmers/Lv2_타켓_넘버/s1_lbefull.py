answer = 0

def dfs(idx, s, numbers, target):
    global answer
    if idx == len(numbers):             # 더 이상 고를 정수가 없을 경우
        if s == target:                 # 현재까지 연산 결과가 target과 같다면
            answer += 1                 # 결과 +1
        return
    
    dfs(idx + 1, s + numbers[idx], numbers, target)     # 아직 정수가 남았다면 각각 더하고 빼서 재귀
    dfs(idx + 1, s - numbers[idx], numbers, target)


def solution(numbers, target):
    global answer
    dfs(0, 0, numbers, target)
    return answer


# print(solution([4, 1, 2, 1], 4))
