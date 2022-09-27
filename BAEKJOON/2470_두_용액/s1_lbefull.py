N = int(input())
arr = list(map(int, input().split()))
arr.sort()

abs_answer = 2000000002
answer = [1000000001, 1000000001]
l = 0
r = N - 1
while l < r:
    sum_arr = arr[l] + arr[r]

    if abs_answer > abs(sum_arr):
        abs_answer = abs(sum_arr)
        answer = [arr[l], arr[r]]
    
    if sum_arr < 0:
        l += 1
    else:
        r -= 1

print(*answer)
