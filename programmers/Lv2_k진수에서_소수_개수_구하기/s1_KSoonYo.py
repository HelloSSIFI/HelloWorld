import math

# 약수의 성질로 소수를 판별하는 것이 중요 point

def is_prime(value):
    if value <= 1:
        return False
    
    for i in range(2, int(math.sqrt(value) + 1)):    
        if value % i == 0:
            return False
    return True
            
    return prime_ref
    

def solution(n, k):
    answer = -1

    # k 진수 변환
    number = ''

    t = n
    while t:
        if k == 10:
            number = str(n)
            break
            
        remain = t % k
        number = str(remain) + number
        t //= k
        

    # 문자열 순회 후 분절 -> count
    nums = []
    for num in number.split('0'):
        if num:
            nums.append(int(num))
    
    cnt = 0
    for num in nums:
        if is_prime(num):
            cnt += 1
    answer = cnt
    return answer