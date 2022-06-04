h, w = map(int, input().split())
b_list = list(map(int, input().split()))
ans = 0

for i in range(1, w-1):
    left_wall = max(b_list[:i])
    right_wall = max(b_list[i+1:])

    max_height = min(left_wall, right_wall)

    if b_list[i] < max_height:
        ans += max_height - b_list[i]

print(ans)