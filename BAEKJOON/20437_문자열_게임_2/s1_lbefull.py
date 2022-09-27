from collections import defaultdict
import sys
input = sys.stdin.readline


answer = []
for tc in range(int(input())):
    W = input().strip()
    K = int(input())
    word_idx = defaultdict(list)
    ans1 = len(W) + 1
    ans2 = 0
    for i in range(len(W)):                                     # 각 문자를 key로 해당 문자가 있는 위치 인덱스를 value 리스트에 저장
        word_idx[W[i]].append(i)
    
    for v in word_idx.values():
        for i in range(K - 1, len(v)):                          # 해당 단어가 K번 이상 나왔으면
            ans1 = min(ans1, v[i] - v[i - K + 1] + 1)           # K 만큼 차이나는 두 인덱스를 빼서 최대값과 최소값을 찾아줌
            ans2 = max(ans2, v[i] - v[i - K + 1] + 1)
    
    if ans2 == 0:
        answer.append('-1\n')
    else:
        answer.append(f'{ans1} {ans2}\n')

print(''.join(answer))
