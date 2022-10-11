def solution(numbers):
    answer = []
    for num in numbers:
        # 짝수인 경우 가장 마지막 비트가 무조건 0
        # 따라서 1 더한 후 append
        if num%2==0:
            answer.append(num+1)

        # 홀수의 경우 0이 나오는 가장 빠른 위치를 1로 바꾸고 그 다음 비트가 0이면
        # 최대 2개만 치환하여 바꾼 가장 작은 수 완성
        else:
            word = '0'+bin(num)[2:]
            i = word.rfind('0')

            word = word[:i] + '10' + word[i+2:]
            answer.append(int(word, 2))

    return answer

print(solution([2, 7]))