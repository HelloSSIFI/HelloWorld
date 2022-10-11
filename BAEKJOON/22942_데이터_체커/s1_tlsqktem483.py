"""
STACK 이용해서 관리 => 시간초과
"""
N = int(input())
c = []
min_v, max_v = float('inf'), 0
for _ in range(N):
    x, r = map(int, input().split())
    min_v, max_v = min(min_v, x-r), max(max_v, x+r)
    c.append([x, r])
arr = [[] for _ in range(max_v-min_v+1)]

for x, r in c:
    l, r = x - r - min_v, x + r - min_v
    for i in range(l, r+1):
        arr[i].append([x, r-l+1])
for i in range(len(arr)):
    arr[i].sort(key=lambda x: x[1], reverse=True)

stack = []
checked = []

for i in range(len(arr)):
    if not arr[i]:
        continue
    for x in arr[i]:
        if x not in checked:
            stack.append(x)
            checked.append(x)
    if i < len(arr)-1 and arr[i] != arr[i+1]:
        pop_len = 0
        pop_list = []
        for x in arr[i]:
            if x not in arr[i+1]:
                pop_len += 1
                pop_list.append(x)
        for _ in range(pop_len):
            x = stack.pop()
            if x not in pop_list:
                print("NO")
                exit(0)
print("YES")