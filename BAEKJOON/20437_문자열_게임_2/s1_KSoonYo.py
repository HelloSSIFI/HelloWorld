###
# python 통과
###

import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    String = input().strip()
    K = int(input())

    if len(String) == 1 and K == 1:
        print(1, 1)
        continue
    
    result = [float('inf'), 0]                         # [3번 규칙, 4번 규칙]

    str_table = defaultdict(list)
    for idx, char in enumerate(String):
        if String.count(char) >= K:
            str_table[char].append(idx)

    for idx_list in str_table.values():
        for j in range(len(idx_list) - K + 1):
            # K로 고정된 길이만큼 슬라이딩하면서 길이 구하기
            length = idx_list[j + K - 1] - idx_list[j] + 1
            if result[0] > length:
                result[0] = length

            if result[1] < length:
                result[1] = length
    
    if result[0] == float('inf') and result[1] == 0:
        print(-1)
    else:
        print(*result)

###
# pypy3 통과
###
import sys
from collections import defaultdict


def get_length(idx, s, k, temp=1):
    length = 1
    target = s[idx]
    for j in range(idx + 1, len(s)):
        length += 1

        if s[j] == target:
            temp += 1

        if temp == k:
            break
    if temp == k and s[idx] == s[idx + length - 1]:
        return length

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    String = input().strip()
    K = int(input())

    if len(String) == 1 and K == 1:
        print(1, 1)
        continue
    
    result = [float('inf'), 0]                         # [3번 규칙, 4번 규칙]

    str_table = defaultdict(int)
    for char in String:
        str_table[char] += 1


    for idx, char in enumerate(String):
        if str_table[char] >= K:
            length = get_length(idx, String, K)
            if length:
                result[0] = min(result[0], length)
                result[1] = max(result[1], length)

    
    if result[0] == float('inf') and result[1] == 0:
        print(-1)
    else:
        print(*result)
    