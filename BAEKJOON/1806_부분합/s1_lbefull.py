N, S = map(int, input().split())
num = list(map(int, input().split()))
sum_num = 0
result = 100001

front = 0           # 부분수열 중 가장 오른쪽 인덱스
rear = -1           # 부분수열 중 가장 왼쪽 -1 인덱스

while front < N:
    if sum_num + num[front] - num[rear + 1] >= S:                                   # 가장 왼쪽 수를 빼도 S를 넘으면
        rear += 1                                                                   # 빼주고 인덱스+1 후 다음 반복
        sum_num -= num[rear]
        continue
    
    if sum_num + num[front] - num[rear + 1] < S and sum_num + num[front] >= S:      # 가장 왼쪽수를 더해야만 S를 넘는다면
        result = min(result, front - rear)                                          # result 갱신
    
    sum_num += num[front]                                                           # 가장 오른쪽 수를 더해주고 인덱스+1
    front += 1

if result == 100001:                # 반복이 끝나도 result가 그대로이면
    result = 0                      # 찾을 수 없다는 뜻이므로 0으로 바꿔줌

print(result)
