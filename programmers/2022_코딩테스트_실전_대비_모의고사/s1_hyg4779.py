def solution(X, Y):
    ans = ''
    tmp = set(X) if len(set(X)) < len(set(Y)) else set(Y)

    for num in tmp:
        ans += num*min(X.count(num), Y.count(num))
    if not ans:
        return '-1'
    else:
        ans = ''.join(sorted(ans, reverse=True)).lstrip('0')
        return '0' if not ans else ans