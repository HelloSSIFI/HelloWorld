from collections import deque
import math
N = int(input())

prime = deque(['2', '3', '5', '7'])
result = []
while prime:
    s = prime.popleft()
    if len(s)==N:
        result.append(s)
        continue

    for i in range(1, 10, 2):
        tmp = s + str(i)
        num = int(math.sqrt(int(tmp)))

        for i in range(2, num+1):
            if not int(tmp)%i:break
        else:
            prime.append(tmp)
for res in result:
    print(res)