def solution(msg):
    answer = []
    LZW = {chr(i + 64): i for i in range(1, 27)}

    words, cnt = '', 27                     # 사전에 1 ~ 26까지 1단어 알파벳이 들어가 있으므로 27부터 시작
    for c in msg:                           # msg의 한 단어씩 순회
        words_add = words + c               # 현재까지 저장된 words에 현재 단어 c를 더해서 words_add에 저장

        if words_add in LZW:                # words_add가 LZW에 들어있다면
            words = words_add               # 다음 단어가 들어있는지 확인하기위해 words 갱신 후 다음 반복
            continue

        answer.append(LZW[words])           # words_add가 LZW에 들어있지 않다면
        LZW[words_add] = cnt                # words 까지는 LZW에 들어있었으므로 words의 사전 번호를 answer에 추가
        cnt += 1                            # 사전(LZW)에 새로운 단어 words_add 추가하고 cnt번호를 1증가
        words = c                           # 사전에 새로운 단어를 추가했으므로 현재 단어부터 다시 단어를 확인해야 하므로 words의 값을 c로 변경

    answer.append(LZW[words])               # 반복이 끝나고 마지막 단어가 추가되지 않았으므로 저장된 words의 사전 번호를 answer에 추가
    return answer


# print(solution("KAKAO"))
