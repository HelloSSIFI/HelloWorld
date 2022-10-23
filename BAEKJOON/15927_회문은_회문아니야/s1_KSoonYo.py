
S = input()
L = len(S)


# 문자열 전체가 회문이 아닌 경우
# 문자열 하나도 팰런드롬
isPalind = True

p1 = 0
p2 = L - 1
while p1 < p2:
    if S[p1] != S[p2]:
        isPalind = False
        print(L)
        break
    p1 += 1
    p2 -= 1

# 문자열 전체가 회문인 경우
# 앞이나 뒤에서 문자 하나를 뺌
# 문자를 뺐는데도 회문이면 모든 경우에 대해서 팰런드롬
p1 = 0
p2 = L - 2
while isPalind and p1 < p2:
    if S[p1] != S[p2]:
        isPalind = False
        print(L - 1)
        break
    p1 += 1
    p2 -= 1

if isPalind:
    print(-1)

