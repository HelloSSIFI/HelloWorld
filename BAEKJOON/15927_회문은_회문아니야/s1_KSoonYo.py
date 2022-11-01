S = input()
L = len(S)


# 문자열 전체가 같은 문자로만 이루어져있는 경우
if len(set(S)) == 1:
    print(-1)
    exit()

# 문자열 전체가 회문이 아닌 경우
p1 = 0
p2 = L - 1
while p1 <= p2:
    if S[p1] != S[p2]:
        print(L)
        exit()
    p1 += 1
    p2 -= 1

# 문자열 전체가 회문인 경우
# 앞이나 뒤에서 문자 하나를 뺌
print(L - 1)
