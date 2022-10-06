def solution(numbers):
    answer = []

    def func(num):
        if num % 2 == 0:
            return num+1

        bin_n = list('0'+bin(num)[2:])
        len_n = len(bin_n)

        for i in range(len_n-1, -1, -1):
            if bin_n[i] == '0':
                bin_n[i] = '1'
                for j in range(i+1, len_n):
                    if bin_n[j] == '1':
                        bin_n[j] = '0'
                        return int(''.join(bin_n), 2)

    for n in numbers:
        answer.append(func(n))
    return answer


print(solution([2, 7]))