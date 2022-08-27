from collections import deque

def is_prime(value):
    if value <= 1:
        return False
    
    for i in range(2, int(value ** 0.5) + 1):
        if value % i == 0:
            return False
    return True


N = int(input())
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
q = deque([(1, '2'), (1, '3'), (1, '5'), (1, '7')])                             # (자릿수, 숫자 표현 문자열)
while q:
    length, num = q.popleft()
    if length == N:
        print(num)
        continue
    temp = num
    for number in numbers:
        temp += number
        if is_prime(int(temp)):
            q.append((length + 1, temp))
        temp = num
