def solution(prices):
    length = len(prices)
    stack = []
    answer = [0] * length
    # stack을 이용한 풀이
    for i in range(length):
        while stack != [] and stack[-1][1] > prices[i]:
            idx, _ = stack.pop()
            answer[idx] = i - idx

        stack.append([i, prices[i]])

    for idx, val in stack:
        answer[idx] = length - 1 - idx

    return answer