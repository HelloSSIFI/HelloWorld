def solution(number, k):
    answer = [number[0]]                                        # 첫 번째 숫자를 정답 문자열에 넣고 시작
    for i in range(1, len(number)):                             # 두 번째 숫자부터 반복
        while k > 0 and answer and number[i] > answer[-1]:      # k가 남아있고 정답 문자열 비어있지 않고, 현재 숫자가 정답 문자열 마지막 숫자보다 큰 동안 반복
            answer.pop()                                        # 정답 문자열에서 마지막 숫자를 지워주고
            k -= 1                                              # k를 1 줄여줌
        answer.append(number[i])                                # 현재 숫자를 넣어줌

    for _ in range(k):                                          # 위 반복이 끝나고 남아있는 k가 있으면
        answer.pop()                                            # 그만큼 뒤에서 삭제

    return ''.join(answer)


# print(solution('1924', 2))
