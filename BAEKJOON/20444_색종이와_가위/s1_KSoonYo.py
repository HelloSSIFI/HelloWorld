
n, k = map(int, input().split())

# 가로 길이 x 세로 길이 = 색종이 개수
# 가로로 자르면 -> 세로 길이 + 1, 세로로 자르면 -> 가로 길이 + 1
# (가로 길이 - 1) + (세로 길이 - 1) = 자른 횟수
# 자른 횟수가 4라면, 가로 - 1 및 세로 - 1 길이 경우의 수는 (0, 4), (1, 3), (2, 2) -> 즉 (0, n), (1, n-1), (2, n-2) ... ...
# 가로 - 1 = 0 and 세로 - 1 = 4일때 가로 길이는 1, 세로 길이는 5 -> 색종이는 1 x 5 = 5
# 이분 탐색으로 k 여부 판별(0부터 n까지 정렬 되어있기 때문에 가능)


left = 0
right = n
while left <= right:
    m = (left + right) // 2
    
    value = (m + 1) * (n - m + 1)
    if value == k:
        print('YES')
        exit()
    
    if value > k:
        right = m - 1
    else:
        left = m + 1
print('NO')
