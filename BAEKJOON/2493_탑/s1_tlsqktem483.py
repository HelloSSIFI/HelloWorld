"""
예상
N <= 500,000 => O(alpha*N) 으로 풀이
O(N*N) 으로 풀이 => 시간초과
60*N 까지 가능할 것

풀이
Stack 을 활용한 최대값 보존
"""
N = int(input())
towel = list(map(int, input().split()))
ans = []
stack = []

for i in range(N):
    while stack:
        if stack[-1][1] > towel[i]:
            ans.append(stack[-1][0]+1)
            break
        else:
            stack.pop()
    if not stack:
        ans.append(0)
    stack.append([i, towel[i]])

print(*ans)