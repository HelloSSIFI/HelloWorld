def solution(X, Y):
    X = sorted(X, reverse=True)
    Y = sorted(Y, reverse=True)
    if X in Y:
        return X
    elif Y in X:
        return Y
    if len(X) > len(Y):
        A = list(X)
        B = list(Y)
    else:
        A = list(Y)
        B = list(X)
    visited = [False] * len(B)
    answer = ''

    for a in A:
        if visited == [True] * len(B):
            break
        for b in range(len(B)):
            if a == B[b] and not visited[b]:
                answer += a
                visited[b] = True
                break
    if not answer:
        answer = "-1"
    elif answer == "0" * len(answer):
        answer = "0"
    return answer


print(solution("100", "2345"))
print(solution("100", "203045"))
print(solution("100", "123450"))
print(solution("12321", "42531"))
print(solution("5525", "1255"))