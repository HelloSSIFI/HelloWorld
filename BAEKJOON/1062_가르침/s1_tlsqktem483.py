"""
Bit Masking
Time : 2160ms
"""
from itertools import combinations
n, k = map(int, input().split())
s_list = list(input() for _ in range(n))
if k < 5:
    print(0)
else:
    n_char = {'a', 'c', 'i', 'n', 't'}      # 필수 문자들
    alpha_dict = {alpha:number for number, alpha in enumerate((set(map(chr, range(ord('a'), ord('z')+1))) - n_char))}       # 필수 문자 제외 딕셔너리
    bit_list = []       # Input 문자열
    count = 0

    for i in range(n):
        temp = 0
        for a in set(s_list[i]) - n_char:
            temp |= (1 << alpha_dict[a])        # Bit masking
        bit_list.append(temp)

    bi_numbers = (2**j for j in range(len(alpha_dict.keys())))      # 총 21개 알파벳에 따른 2진 범위
    for comb in combinations(bi_numbers, k-5):
        temp_sentence = sum(comb)

        temp_count = 0
        for compare in bit_list:        # Input 문자열과 비교하여 count
            if temp_sentence & compare == compare:
                temp_count += 1

        count = max(temp_count, count)
    print(count)