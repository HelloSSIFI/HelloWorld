A, B = map(int, input().split())

cnt = 1                         # 현재 인덱스의 숫자
result = 0                      # 구간합을 저장할 변수
temp = 1                        # 현재 인덱스가 어느 숫자인지 판별할 임시 변수

for i in range(A, B + 1):       # A ~ B 탐색
    while temp < i:             # temp 구간을 i와 맞춰줌
        cnt += 1                # 예를들어 4번째 인덱스라면 temp에 +1 +2 < 인덱스(4) <= +1 +2 +3
        temp += cnt             # 위 구간에 있어야 하며 그 때의 숫자는 3

    result += cnt               # 현재 구간의 숫자를 result에 더해줌

print(result)
