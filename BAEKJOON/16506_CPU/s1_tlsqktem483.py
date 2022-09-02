import sys
input = sys.stdin.readline

N = int(input())

S = [list(input().split()) for _ in range(N)]

for n in range(N):
    s = S[n][0]
    ans = ''
    # bit 0-3
    if s[:2] == 'AD':
        ans += '0000'
    elif s[:2] == 'SU':
        ans += '0001'
    elif s[:2] == 'MO':
        ans += '0010'
    elif s[:2] == 'AN':
        ans += '0011'
    elif s[:2] == 'OR':
        ans += '0100'
    elif s[:2] == 'NO':
        ans += '0101'
    elif s[:2] == 'MU':
        ans += '0110'
    elif s[:2] == 'LS' and s[4] == 'L':
        ans += '0111'
    elif s[:2] == 'LS' and s[4] == 'R':
        ans += '1000'
    elif s[:2] == 'AS':
        ans += '1001'
    elif s[:2] == 'RL':
        ans += '1010'
    elif s[:2] == 'RR':
        ans += '1011'

    # bit 4-5
    if s[-1] == 'C':
        ans += '10'
    else:
        ans += '00'

    # bit 6-8
    temp = bin(int(S[n][1]))[2:]
    for _ in range(3):
        if len(temp) == 3:
            break
        temp = '0' + temp
    ans += temp

    # bit 9-11
    if s[:2] in ['MO', 'NO']:
        ans += '000'
    else:
        temp = bin(int(S[n][2]))[2:]
        for _ in range(3):
            if len(temp) == 3:
                break
            temp = '0' + temp
        ans += temp

    # bit 12-15
    if ans[4] == '0':
        temp = bin(int(S[n][-1]))[2:]
        for _ in range(3):
            if len(temp) == 3:
                break
            temp = '0' + temp
        ans += temp + '0'
    else:
        temp = bin(int(S[n][-1]))[2:]
        for _ in range(4):
            if len(temp) == 4:
                break
            temp = '0' + temp
        ans += temp
    print(ans)