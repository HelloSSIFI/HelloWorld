# N, M = map(int, input().split())
#
# tmp = min(N, M)
#
# max_v = 1
# min_v = 1
#
# while tmp:
#
#     if N%tmp == 0 and M%tmp == 0:
#         N //= tmp
#         M //= tmp
#         max_v *= tmp
#         break
#     tmp -= 1
#
#
# min_v = max_v*N*M
#
#
#
# print(max_v)
# print(min_v)

N, M = map(int, input().split())

tmp = []
for i in range(1, min(N, M) + 1):
    if N % i == 0 and M % i == 0:
        tmp.append(i)

print(max(tmp))
print(max(tmp) * (N // max(tmp)) * (M // max(tmp)))