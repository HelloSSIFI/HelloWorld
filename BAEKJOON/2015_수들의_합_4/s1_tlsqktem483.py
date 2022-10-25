ans = 0
N, K = map(int, input().split())
a = [0] + list(map(int, input().split()))
n_dict = {}
prefix = [0]

for i in range(1, N+1):
    prefix.append(prefix[i-1] + a[i])

for i in range(N+1):
    ans += n_dict.get(prefix[i]-K, 0)
    n_dict[prefix[i]] = n_dict.get(prefix[i], 0) + 1

print(ans)