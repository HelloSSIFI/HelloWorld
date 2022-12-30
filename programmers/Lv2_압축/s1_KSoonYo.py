def solution(msg):
    # key point : two pointer

    answer = []
    table = {}                              # 사전
    word = ord('A')                         
    for i in range(26):                     # 초기 사전 셋팅 (색인 1부터 26까지)
        table[chr(word + i)] = i + 1        # 단어(key) : 색인 숫자(value)

    idx = 0                                 # pointer1
    plus = 1                                # 색인 추가, offset = 26
    while idx < len(msg):       
        j = idx                             # pointer2
        w = msg[j]                          # 시작 글자
        k = 0                               # 시작 글자에서 추가되는 글자 개수
        while table.get(w):                 # w가 사전에 없을 때까지 계속 글자를 추가
            j += 1
            k += 1
            if j >= len(msg):               # j가 입력값 길이를 벗어난다면 break
                break
                
            w += msg[j]                     # 현재 시작 글자에서 msg의 j번째 글자 추가
        answer.append(table[w[:k]])         # 반복의 마지막까지 추가된 개수에서 하나를 뺀 만큼 사전에서 색인 검색
        if not table.get(w):                # k번째까지 추가된 글자 w가 사전에 없다면
            table[w] = 26 + plus            # 사전에 색인 추가
        plus += 1                           
        idx += k                            # pointer1 jump(다음 반복문은 w에 마지막으로 추가된 글자에서 시작)
    return answer