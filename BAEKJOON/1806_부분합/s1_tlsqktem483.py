"""
투포인터 (left, right)
"""
n, s = map(int, input().split())
n_list = list(map(int, input().split()))
left, right = 0, 0
c_sum = 0

ans = n + 1

while True:
    if c_sum >= s:
        ans = min(ans, right - left)
        c_sum -= n_list[left]
        left += 1
    elif right >= n:
        break
    else:
        c_sum += n_list[right]
        right += 1

if ans == n+1:
    print(0)
else:
    print(ans)