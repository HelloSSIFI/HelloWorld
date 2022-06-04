
H, W = map(int, input().split())        # H: 최대 높이, W: 가로 너비


blocks = list(map(int, input().split()))

left_start = 0
right_start = 0

ans = 0

# 왼쪽 시작점
for left_idx in range(W):
    if blocks[left_idx]:
        left_start = left_idx
        break

# 오른쪽 시작점
for right_idx in range(W-1, -1, -1):
    if blocks[right_idx]:
        right_start = right_idx
        break
    
if left_start == right_start:
    print(ans)

else:
    left_water_bound  = [0 for _ in range(W)]
    right_water_bound = [0 for _ in range(W-1, -1, -1)]
    final_water_bound = [0 for _ in range(W)]

    total_water = 0

    # 왼쪽부터 블록 수면 경계면
    left_height = blocks[left_start]
    for left_idx in range(left_start, W):
        if left_height < blocks[left_idx]:
            left_height = blocks[left_idx]
        left_water_bound[left_idx] = left_height
    
    # print('left_water_bound: ', left_water_bound)

    # 오른쪽부터 블록 수면 경계면
    right_height = blocks[right_start]
    for right_idx in range(right_start, -1, -1):
        if right_height < blocks[right_idx]:
            right_height = blocks[right_idx]
        right_water_bound[right_idx] = right_height

    # print('right_water_bound: ', right_water_bound)


    # 최종 수면 경계    
    for idx in range(W):
        if left_water_bound[idx] != 0 and right_water_bound[idx] != 0:
            final_water_bound[idx] = min(left_water_bound[idx], right_water_bound[idx])


    # print('final_water_bound: ', final_water_bound)

    # 빗물의 양 누적합
    for water_idx in range(W):
        total_water += final_water_bound[water_idx] - blocks[water_idx]

    ans = total_water
    print(ans)
