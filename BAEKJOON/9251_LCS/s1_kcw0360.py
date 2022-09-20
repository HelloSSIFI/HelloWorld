import sys
input = sys.stdin.readline


a = input().rstrip()    # \n이 들어가지 않게 해줘야 한다.
b = input().rstrip()

LCS = [[0 for _ in range(len(a)+1)] for _ in range(len(b)+1)]

for i in range(1, len(b)+1):
    for j in range(1, len(a)+1):
        if b[i-1] == a[j-1]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i-1][j], LCS[i][j-1])

print(LCS[-1][-1])