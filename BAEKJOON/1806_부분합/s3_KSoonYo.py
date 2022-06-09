# 투 포인터 방식

N, S = map(int, input().split())
numbers = list(map(int, input().split()))
start = end = 0
min_length = N + 1
sub_total = numbers[0]

while True:
    if start == N or end == N:
        break
    
    if sub_total >= S:                              # 부분합이 S 이상인 경우
        length = end - start + 1                    # 길이를 구하고
        min_length = min(min_length, length)        
        sub_total -= numbers[start]                 # 현재의 start 부분에 있는 애를 빼준 뒤에  
        start += 1                                  # start 포인터를 한 칸 뒤로 민다.
    else:                                           # 현재의 부분합이 S보다 작은 경우
        end += 1                                    # end 포인터를 한 칸 뒤로 밀어준 뒤에
        if end < N:                                 # end 가 N보다 작다면
            sub_total += numbers[end]               # 부분합에 더한다.

if min_length == (N + 1):
    print(0)
else:
    print(min_length)
