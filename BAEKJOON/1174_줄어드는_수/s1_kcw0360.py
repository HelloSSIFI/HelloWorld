from itertools import combinations

N = int(input())

numbers = []

if N > 1023:    # 9876543210은 numbers에서 idx가 1022(N == 1023)일 때 이므로 이 이상 큰 수는 감소하는 수 불가능
    print(-1)
else:
    for length in range(1, 11):    # 자릿수 1~10 경우를 찾기 위함
        for temp in combinations(range(10), length):    # 중복되지 않은 수의 조합을 모두 찾는다.
            number = list(temp)
            number.sort(reverse=True)    # 내림차순
            num = ''.join(map(str, number))    # 하나의 숫자로 변환
            numbers.append(int(num))    # 숫자로 바꿔 리스트에 추가

    numbers.sort()    # 오름차순으로 정렬, N = idx

    print(numbers[N-1])    # N이 1일 때 값이 0이 출력 되어야 한다