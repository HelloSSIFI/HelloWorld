H, W = map(int, input().split())        # 높이, 너비
wall = list(map(int, input().split()))      # 벽의 높이들

result = 0

'''
현재 위치에서 좌우로 가장 큰 벽을 찾고,
그 벽에서 낮은 벽의 높이 = low
low > 현재 인덱스 벽 높이 = 빗물이 담김
result += low
'''

for i in range(1, W-1):
    left = max(wall[:i])
    right = max(wall[i+1:])
    low = min(left, right)

    if low > wall[i]:
        result += low - wall[i]

print(result)