N = int(input())
num_list = list(map(int, input().split()))
prime_number = [1] * 1001           # 현재 인덱스가 소수인지 판별할 배열
prime_number[0] = 0                 # 0과 1은 소수가 아니므로 0으로 변경
prime_number[1] = 0

for i in range(2, 1000):            # 2~1000까지 순회
    if not prime_number[i]:         # 만약 현재 수가 소수가 아니면 다음 반복
        continue
    
    j = 2                           # 현재 수가 소수일 경우
    while i * j <= 1000:            # 그 수의 1000이하의 배수는 모두 소수가 아님 표시
        prime_number[i * j] = 0
        j += 1

result = 0
for num in num_list:                # 입력받은 숫자 배열 순회
    if prime_number[num]:           # 소수일 경우 result +1
        result += 1

print(result)
