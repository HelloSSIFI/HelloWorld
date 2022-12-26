def solution(msg):
    answer = []
    index = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
             'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19,
             'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}    # 사전
    nxt_idx = 27    # 다음 추가 될 단어의 색인 번호
    now = 0    # 현재 msg의 idx

    while now < len(msg):    # now가 msg - 1이 됬을 때 종료
        temp = ''    # 현재 구성하고 있는 글자
        nxt = now
        temp += msg[nxt]    # 글자 추가

        while nxt < len(msg):
            if temp in index:    # 사전에 temp 글자가 존재하는 경우
                nxt += 1    # 다음 단어로 넘어가기 위해 +1
                if nxt == len(msg):    # 마지막 글자인 경우 while 빠져 나가기
                    break
                temp += msg[nxt]    # temp에 글자 추가
            else:    # 사전에 temp가 존재하지 않는 경우
                index[temp] = nxt_idx    # 사전에 추가
                temp = temp[:-1]    # 이전 단어로 복귀
                nxt_idx += 1    # 색인 번호 +1
                break

        answer.append(index[temp])    # 정답에 temp의 색인 번호 추가
        now = nxt    # now를 nxt로 변경

    return answer