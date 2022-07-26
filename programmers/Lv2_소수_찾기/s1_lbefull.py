from itertools import permutations


def is_prime(n):                                # 소수 판별 함수
    if n < 2:                                   # 0, 1 이라면 False
        return False
    
    for i in range(2, int(n ** 0.5) + 1):       # 입력받은 수의 제곱근까지 반복
        if n % i == 0:                          # 나누어 떨어지는 수가 있다면 False
            return False                        # 그 이외에는 True
    return True


def solution(numbers):
    N = len(numbers)
    pos = set()

    for i in range(1, N + 1):                   # 1~N 까지 순열 선택하여
        for el in permutations(numbers, i):     # 정수로 변환하여 pos에 넣어줌
            pos.add(int(''.join(el)))
    
    answer = 0
    for p in pos:                               # pos 순회
        if is_prime(p):                         # 소수이면 answer+1
            answer += 1
    
    return answer


# print(solution('17'))



############  직접 permutations 구현  #########################

# def perm(cnt, choice, numbers):
#     if len(choice) == cnt:
#         pos.add(int(''.join(choice)))
#         return
    
#     for i in range(N):
#         if not visited[i]:
#             choice.append(numbers[i])
#             visited[i] = 1
#             perm(cnt, choice, numbers)
#             visited[i] = 0
#             choice.pop()


# def is_prime(n):
#     if n < 2:
#         return False
    
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# def solution(numbers):
#     global pos, N, visited
#     N = len(numbers)
#     pos = set()
#     visited = [0] * N

#     for i in range(N):
#         perm(i + 1, [], numbers)
    
#     answer = 0
#     for p in pos:
#         if is_prime(p):
#             answer += 1
    
#     return answer
