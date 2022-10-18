def dfs(par):
    global leaf

    if par == del_node:
        return

    chi = n_dict[par]
    if not chi or chi == [del_node]:
        leaf += 1
        return

    for c in chi:
        dfs(c)


N = int(input())
n_dict = {i: [] for i in range(N)}
n_arr = list(map(int, input().split()))
del_node = int(input())
root = 0
for i in range(N):
    parent = n_arr[i]
    if parent != -1:
        n_dict[parent].append(i)
    else:
        root = i

leaf = 0
dfs(root)
print(leaf)