def is_prime(n):                                # 소수 판별 함수
    if n == 1:                                  # 1은 False
        return False

    for i in range(2, int(n ** 0.5) + 1):       # 2 이상부터는 제곱근까지 반복하면서
        if n % i == 0:                          # 나누어 떨어지면 False
            return False                        # 아니라면 True
    return True


def find_prime(n, cnt):                         # 왼쪽부터 한 자리씩 소수만 찾아나갈 예정
    if cnt == N:                                # N 자리수를 모두 골랐다면
        print(n)                                # 출력
        return
    
    for i in range(10):                         # 현재 자리에 0 ~ 9 까지 더해보면서
        if is_prime(n * 10 + i):                # 소수일경우
            find_prime(n * 10 + i, cnt + 1)     # 자리수를 늘려서 재귀


N = int(input())
for i in range(2, 10):                          # 맨 앞자리는 소수인 2부터 시작
    if is_prime(i):
        find_prime(i, 1)
