def solution(elements):
    answer = set()
    length = len(elements)
    elements += elements
    for i in range(length):
        for j in range(1, length+1):
            answer.add(sum(elements[i:i+j]))

    return len(answer)