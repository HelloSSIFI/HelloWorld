n, k = map(int, input().split())

# 이진 탐색을 위한 좌우 값
l = 0
r = n

while l < r:
    mid = (l + r) // 2    # 중간점

    temp = (mid + 1) * (n - mid + 1)    # 색종이 조각 수

    if temp == k:    # 목표 조각 수와 같으면 YES
        print('YES')
        exit(0)

    if temp > k:    # 목표 조각수 보다 많으면 큰 값을 mid로 치환
        r = mid
    else:    # 작은 경우 작은 쪽 값을 mid+1로 치환
        l = mid + 1

print('NO')    # 불가능한 경우 NO