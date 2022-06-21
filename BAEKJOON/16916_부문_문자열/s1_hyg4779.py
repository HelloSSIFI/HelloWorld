'''
S = input()
P = input()
print(int(P in S))
'''


def kmp_table(word):

    '''
    KMP 전 패턴 처리 함수
    패턴 테이블 return
    '''

    l = len(word)
    table = [0 for _ in range(l)]     # 정보 저장 테이블

    idx = 0                         # tab 값을 불러 오고, word 인덱스 접근
    for i in range(1, l):           # tab에 값 저장 하기 위해 i 인덱스 활용
        # idx가 0이 되거나, i와 idx의 word 접근 값이 같이질 때까지 진행
        while idx > 0 and word[i] != word[idx]:
            idx = table[idx - 1]

        # 값이 일치하는 경우, idx 값을 +1 하고, 그 값을 tb에 저장
        if word[i] == word[idx]:
            idx += 1
            table[i] = idx

    return table


def KMP(text, word):
    table = kmp_table(word)             # 전처리 된 테이블 불러오기

    res = []                            # 결과를 만족하는 인덱스 시점을 기록하는 리스트
    idx = 0

    for i in range(len(text)):
        # text와 word가 일치하지 않는 경우, idx를 table을 활용해 값 변경
        while idx > 0 and text[i] != word[idx]:
            idx = table[idx - 1]

        # 인덱스 값이 일치한다면 idx + 1,
        # idx가 패턴 끝까지 도달했다면, 시작 인덱스 값을 계산하여 추가 후 idx값 table의 인덱스에 접근하여 변경

        if text[i] == word[idx]:
            if idx == len(word)-1:
                res.append(i - len(word) + 2)
                idx = table[idx]
            else:
                idx += 1

    return res


text = input()
word = input()
table = [0]*len(text)                    # 문자열 접두사 접미사 일치하는 개수 확인 배열

# https://youtu.be/yWWbLrV4PZ8 : KMP알고리즘-나동빈


def make_table(wrd):
    idx = 0                             # 접두사 인덱스
    for i in range(1, len(wrd)):
        if idx > 0 and wrd[i] != wrd[idx]:  # 접두사 인덱스와 가장 마지막 문자가 일치하지 않으면, 접두사 인덱스 초기화
            idx = 0

        if wrd[i] == wrd[idx]:              # 현재 접두사와 가장 마지막 문자가 일치한다면
            idx += 1                        # 접두사 인덱스 증가
            table[i] = idx                  # 테이블에 접두사 인덱스 값 저장


def solution(txt, wrd):

    make_table(word)
    j = 0

    for i in range(len(txt)):

        while j > 0 and txt[i] != wrd[j]:
            j = table[j-1]

        if txt[i] == wrd[j]:

            if j == len(wrd)-1:
                return True

            else:
                j += 1
    return False