import sys
input = sys.stdin.readline

W = input().strip()        # 문자열
B = list(input().strip())        # 폭파문자
lb = len(B)
stack = []
# lw, lb = len(W), len(B)
# i, j = 0, 0
# arr = [0]*lw
# pre = ''

# while i < lw:
#
#     if W[i] == B[j]:
#         i += 1
#         j += 1
#
#         if j == lb:
#             W = pre + W[i:]
#             i -= j
#             if arr[i]:
#                 i -= arr[i]
#                 pre = pre[:-arr[i]-1]
#             lw = len(W)
#             j = 0
#
#     elif W[i] != B[j]:
#         if j:
#             arr[i] = j
#             pre += W[i-j:i]
#             j = 0
#         else:
#             pre += W[i]
#             i += 1
#
# print(W if W else 'FRULA')

for i in W:
    stack.append(i)
    if len(stack) >= lb:
        if stack[-lb:] == B:
            for _ in range(lb):
                stack.pop()

print(*stack if stack else 'FRULA', sep="")