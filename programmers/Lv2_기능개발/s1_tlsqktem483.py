def solution(p, s):
    ans = []
    while sum(ans) < len(p):
        flag = False
        cnt = 0
        for i in range(sum(ans), len(p)):
            p[i] += s[i]
            if (p[i] >= 100 and i == sum(ans)) or (p[i] >= 100 and flag):
                flag = True
                cnt += 1
            else:
                flag = False
        if cnt:
            ans.append(cnt)
    return ans