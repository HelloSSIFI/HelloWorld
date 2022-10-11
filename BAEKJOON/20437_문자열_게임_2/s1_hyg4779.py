t = int(input())
for tc in range(t):
    W = input()
    k = int(input())
    check = []
    for i in range(len(W)):
        if W.count(W[i]) < k or W[i] in check:continue
        check.append(W[i])