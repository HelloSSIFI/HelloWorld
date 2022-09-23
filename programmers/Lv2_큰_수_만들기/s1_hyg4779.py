def solution(number, k):
    answer = [number[0]]

    for i in range(1, len(number)):
        while k and answer and answer[-1] < number[i]:
            answer.pop()
            k -= 1
        answer.append(number[i])

    for _ in range(k):
        answer.pop()

    return ''.join(answer)