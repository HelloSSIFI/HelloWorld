n = int(input())
nums = list(map(int, input().split()))
nums.sort()

l, r = 0, n-1

result = []
answer = 10e+9+1

while l < r:
    nl, nr = nums[l], nums[r]
    tmp = nl + nr

    if abs(tmp) < answer:
        answer = abs(tmp)
        result = [nl, nr]

    if tmp < 0:
        l += 1
    else:
        r -= 1

print(*result)
