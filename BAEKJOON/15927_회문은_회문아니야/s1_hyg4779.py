'''
65% 시간초과
'''

W = input()

l, r = 0, len(W)
answer = -1

while l <= r:
    mid = (l+r)//2

    for i in range(len(W)-mid+1):
        tmp = W[i:i+mid]
        if W[i:i+mid] != W[i:i+mid][::-1]:
            l = mid+1
            answer = mid
            break
    else:
        r = mid-1

print(answer)

'''
참고: https://recordofwonseok.tistory.com/417
import sys,math
input = sys.stdin.readline

S = input().strip()
l = len(S)
if S == S[0] * l: print(-1) # 길이가 1이거나 같은 문자만 반복되는 경우 무조건 회문
elif S[:l//2][::-1] == S[math.ceil(l/2):]: print(l-1) # S가 회문인 경우 -> S의 길이 - 1이 답
else: print(l) # S가 회문이 아닌 경우 -> S의 길이가 답
'''