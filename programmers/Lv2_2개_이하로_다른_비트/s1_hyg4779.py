def solution(numbers):
    answer = []
    for num in numbers:

        if num%2==0:
            answer.append(num+1)

        else:
            word = '0'+bin(num)[2:]
            i = word.rfind('0')

            word = word[:i] + '10' + word[i+2:]
            answer.append(int(word, 2))

    return answer

print(solution([2, 7]))