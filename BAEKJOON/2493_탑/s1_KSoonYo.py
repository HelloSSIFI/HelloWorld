# stack 사용

N = int(input())
towers = list(map(int, input().split()))
table = [0] * N
stack = [(N - 1, towers[N - 1])]

for i in range(N - 1, -1, -1):
    while stack and stack[-1][1] <= towers[i]:
        received =  stack.pop()[0]
        table[received] = i + 1
    stack.append((i, towers[i]))

print(*table)    
