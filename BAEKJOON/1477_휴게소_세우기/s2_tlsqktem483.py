N, M, L = map(int, input().split())
loc = [0]+list(map(int, input().split()))+[L]
loc.sort()

start, end = 1, L-1
result = 0
while start <= end:
    divide = 0
    mid = (start+end) // 2
    for i in range(1, len(loc)):
        if loc[i]-loc[i-1] > mid:
            divide += (loc[i]-loc[i-1]-1)//mid
    if divide > M:
        start = mid+1
    else:
        end = mid-1
        result = mid
print(result)