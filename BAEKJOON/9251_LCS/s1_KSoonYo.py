# LCS 알고리즘(최장 공통 부분 수열)
# https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence


A = ''
B = ''
for _ in range(2):
    if not A:
        A = input()
    else:
        B = input()

A = '.' + A
B = '.' + B
LCS = [[0] * len(A) for _ in range(len(B))]

for i in range(1, len(B)):
    for j in range(1, len(A)):
        if B[i] == A[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[-1][-1])