from collections import deque
def solution(order):

    n = len(order)

    answer = 0

    # 컨테이너 벨트: 큐
    queue = 1

    # 보조 벨트: 스텍
    stack = []

    # order 순서 인덱스
    idx = 0

    # q가 컨테이너 벨트를 탐색중이거나, 스텍이 남아있다면 반복
    while queue <= n or stack:


        # 현재 뺄 순서가 벨트 앞 순서와 같다면
        if order[idx] == queue:
            queue += 1
            answer += 1
            idx += 1

        # 현재 뺄 순서가 벨트 안 쪽에 있는 상자라면 스텍에 옮김
        elif order[idx] > queue:
            stack.append(queue)
            queue += 1

        # 벨트에 없고
        else:
            # 스텍 맨 앞에서 뺄 수 있다면ㅁ
            if stack and stack[-1] == order[idx]:
                stack.pop()
                answer += 1
                idx +=1

            # 스텍에 있지만 앞에 없다면 break
            elif stack and order[idx] in stack:
                break

    return answer

print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))