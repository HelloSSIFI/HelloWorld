from collections import deque
import math
N = int(input())

# 한 자리 수 소수
prime = deque(['2', '3', '5', '7'])
result = []

# 소수 목록들을 돌며 뒤에 홀 수 들을 추가해보면서 소수 판정 통과시 prime에 추가
while prime:
    s = prime.popleft()
    # 현재 탐색할 소수의 길이가 N이면 result에 추가하고 continue
    if len(s)==N:
        result.append(s)
        continue

    # 소수 만들기
    for i in range(1, 10, 2):
        tmp = s + str(i)
        num = int(math.sqrt(int(tmp)))

        for i in range(2, num+1):
            if not int(tmp)%i:break
        else:
            prime.append(tmp)

for res in result:
    print(res)