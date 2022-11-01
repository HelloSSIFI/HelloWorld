"""
Stack 활용
N <= 1,000,000
main을 pop 하지 않고 pointer 활용
"""
def solution(order):
    answer = 0
    main = [i for i in range(1, len(order)+1)]

    if main == order:
        return len(order)

    stack = []
    pointer = 0
    for o in order:

        if stack and stack[-1] == o:
            stack.pop()
            answer += 1
            continue

        while pointer < len(main) and o != main[pointer]:
            stack.append(main[pointer])
            pointer += 1

        if pointer < len(main) and o == main[pointer]:
            answer += 1
            pointer += 1

        else:
            break

    return answer


print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))