import sys
input = sys.stdin.readline

N = int(input())
arr = [input().strip() for _ in range(N)]
arr.sort(key=len)

answer = 0

for i in range(N):
    for j in range(i+1, N):
        if arr[i]==arr[j][:len(arr[i])]:
            break
    else:
        answer += 1

print(answer)
