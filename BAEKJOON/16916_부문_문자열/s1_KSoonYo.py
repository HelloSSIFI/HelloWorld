# KMP 알고리즘
# 시간복잡도 O(n)
def KMP(s, p):
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j - 1]

        if s[i] == p[j]:
            if j == len(p) - 1:
                return 1
            else:
                j += 1
    
    return 0


# PI 테이블 생성
def make_table(p):
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[j] != p[i]:
            j = table[j - 1]

        if p[j] == p[i]:
            j += 1
            table[i] = j


S  = input()
P = input()
table = [0 for _ in range(len(P))]
make_table(P)
ans = KMP(S, P)
print(ans)
