N = int(input())
if N < 10:
    print(N)
    exit()
num = 10
cnt = 9


def assemble(n, word):
    global cnt

    if n == M:      # 해당 숫자의 길이가 다 되면 감소하는 수인지 검사
        cnt += 1
        if cnt == N:
            print(word)
            exit()
        return

    for i in range(int(word[-1])):
        new = word + str(i)
        assemble(n+1, new)


while num <= 10000000000:
    M = len(str(num))       # 숫자의 길이
    top = str(num)[0]       # 가장 큰 수

    assemble(1, str(top))
    num += 10**(M-1)
else:
    print(-1)


'''
from collections import deque
d = deque()
count = -1
n = int(input())
for i in range(10):
    d.append(i)
while d:
    now_num = d.popleft()
    count += 1

    if count == n:
        print(now_num)
        exit()

    for i in range(now_num%10):
        d.append(now_num*10 + i)

print(-1)
'''