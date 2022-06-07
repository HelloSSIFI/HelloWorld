def solution(n):
    answer = ''
    while n:                        # n이 0이 아닌동안 반복
        if n % 3:                   # 3진수처럼 나머지를 구해서 맨 오른쪽에 붙여줌
            mod = str(n % 3)        # 숫자는 124 이므로 12는 그대로 나머지를 쓰고 0일 경우 4로 치환
        else:
            mod = '4'
        answer = mod + answer
        n = (n - 1) // 3            # 3까지 한묶음이므로 1을 빼서 3으로 나눈 몫으로 다시 반복
    return answer

# print(solution(1))
