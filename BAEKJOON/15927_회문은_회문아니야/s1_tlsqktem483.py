def is_palindrome(s):
    n = len(s) // 2

    flag = False
    if len(s) % 2:
        if s[:n] == list(reversed(s[n+1:])):
            flag = True
    else:
        if s[:n] == list(reversed(s[n:])):
            flag = True
    return flag


S = list(input())

if S == [S[0]]*len(S) or len(S) == 1:
    print(-1)
elif is_palindrome(S):
    print(len(S)-1)
else:
    print(len(S))