answer = 0

def dfs(numbers, target, temp=0, cnt=0):
    global answer

    if cnt == len(numbers) and temp == target:
        answer += 1
        return

    if cnt == len(numbers):
        return

    dfs(numbers, target, temp+numbers[cnt], cnt+1)
    dfs(numbers, target, temp-numbers[cnt], cnt+1)


def solution(numbers, target):
    global answer
    dfs(numbers, target)
    return answer