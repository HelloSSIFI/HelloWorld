from collections import defaultdict
import sys
input = sys.stdin.readline


T = int(input())

ans = []
for t in range(T):
    W = input()
    K = int(input())

    check = defaultdict(list)    # key: 알파벳 문자, value: 문자 위치 idx
    res = []    # 문자 길이 저장

    for idx in range(len(W)):    # 문자의 idx를 check에 저장
        check[W[idx]] += [idx]

    for c in check.values():    # key에 해당하는 value 값들에서 찾아본다.
        for i in range(len(c)):
            try:    # K개 만큼 존재한다면 문자를 idx로 자른 후 길이를 res에 저장
                res.append(len(W[c[i]:c[i+K-1]+1]))
            except:
                break

    if res:
        ans.append('{} {}\n'.format(min(res), max(res)))
    else:
        ans.append('{}\n'.format(-1))

print(''.join(ans))
