def solution(numbers, target):
    ans = 0

    if sum(numbers) < target:           # 가지치기
        return 0

    l = len(numbers)

    def dfs(value, idx):
        nonlocal ans                    # 로컬 변수 가져오기

        if idx == l:                    # 배열 모든 값을 돌으면 검사

            if value == target:
                ans += 1
            return

        dfs(value + numbers[idx], idx+1)        # +, - 재귀
        dfs(value - numbers[idx], idx+1)

    dfs(0, 0)

    return ans