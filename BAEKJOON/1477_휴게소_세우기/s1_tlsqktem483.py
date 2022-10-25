"""
한 구간 다중분할을 고려 안됨
"""
ans = 0
N, M, L = map(int, input().split())
loc = list(map(int, input().split()))
n_list = []
loc += [0] + [1000]
loc.sort()

prev = loc[0]
for i in range(1, len(loc)):
    cur = loc[i]
    n_list.append([prev, cur])
    prev = cur

for _ in range(M):
    n_list.sort(key=lambda x: x[1]-x[0])
    target = n_list[-1]
    new_loc = target[0] + (target[1]-target[0])//2

    n_list[-1] = [target[0], new_loc]
    n_list.append([new_loc, target[1]])

n_list.sort(key=lambda x: x[1]-x[0])
ans = n_list[-1][1]-n_list[-1][0]
print(ans)