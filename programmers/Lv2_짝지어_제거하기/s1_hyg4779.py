from collections import deque

def solution(word):
    word = list(word)                   # 현재 문자 리스트 화
    pre = deque([])                     # 큐에 문자를 담으면서 탐색

    for i in range(len(word)):          # 문자열 탐색
        if pre and pre[0] == word[i]:   # 큐에 문자가 있고, 마지막 문자와 현재 문자가 같다면 pop
            pre.popleft()
        else:
            pre.appendleft(word[i])     # 큐가 비었거나, 문자가 다르다면 큐에 추가
    else:                               # 1회 탐색 후 큐가 비어있다면 1 남은 문자 있다면 0 return
        if pre:return 0
        return 1

print(solution('baabaa'))


def solution(word):
    # 시간초과 코드

    while len(word) > 1:                # word가 1개 이상일 때: 짝지어 제거할 수 있을 때
        idx = 0                         # word를 탐색할 인덱스
        pre = ''                        # 탐색 후 글자를 담을 문자열
        while idx < len(word)-1:        # 현재 문자와 다음 문자가 같다면 인덱스 담지 않고 넘어감
            if word[idx] == word[idx+1]:
                idx += 2

            else:                       # 다르다면 현재 문자만 pre에 담음
                pre += word[idx]
                idx += 1

        else:                           # word 1회 탐색 후 word로 문자 갱신
            word = pre

    else:                               # word가 1개 이하일 때 1개
        if len(word):                   # 남아있으면 0 없다면 1 return
            return 0
        return 1