# 런타임 에러 발생
# 91.7 / 100

def calc(arr, num):
    for n in arr:
        if n % num == 0:
            return 0
    return num

def GCD(arr, temp = 0):                                     # 최대 공약수 구하기
    num1, num2 = arr[0], arr[1]
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    temp = num1
    
    for h in range(2, len(arr)):
        num1, num2 = arr[h], temp
        while num2 != 0:
            num1, num2 = num2, num1 % num2
        temp = num1
    
    return temp

def solution(arrayA, arrayB):
    answer = 0
    arrayA.sort(reverse=True)
    arrayB.sort(reverse=True)
    gcd_A = GCD(arrayA)
    gcd_B = GCD(arrayB)
    
    candidates = {
        'a': 0,
        'b': 0
    }
    for i in range(gcd_A, 0, -1):
        if gcd_A % i == 0 and calc(arrayB, i):              # 조건 1
            candidates['a'] = i
            break
    for j in range(gcd_B, 0, -1):
        if gcd_B % j == 0 and calc(arrayA, j):              # 조건 2
            candidates['b'] = j
            break
    answer = max(candidates.values())
    
    return answer