# 오답

from collections import deque

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

sub_total = numbers[0]
min_length = N + 1
deq = deque([numbers[0]])
flag = False


idx = 1
while idx <= N:
    if len(deq) == 0:
        idx += 1
        continue

    if sub_total >= S:
        min_length = min(min_length, len(deq))
        removed_num = deq.popleft()
        sub_total -= removed_num
        flag = True

    else:
        if flag:
            flag = False

        elif idx < N:
            deq.append(numbers[idx])
            sub_total += numbers[idx]
        
        idx += 1

if min_length == (N + 1):
    min_length = 0

print(min_length)
