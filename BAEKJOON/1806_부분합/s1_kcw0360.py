N, S = map(int, input().split())

numbers = list(map(int, input().split()))

interval_sum = 0
end = 0
result = 100001

# start를 차례대로 증가시키면서 반복
for i in range(N):
    # end를 가능한 만큼 이동시키기
    while interval_sum < S and end < N:
        interval_sum += numbers[end]
        end += 1
    # 부분합이 S 이상일 때 카운트 증가 및 길이 찾기
    cnt = len(range(i, end))
    if interval_sum >= S and result > cnt:
        result = cnt
    interval_sum -= numbers[i]

if result == 100001:
    print(0)
else:
    print(result)