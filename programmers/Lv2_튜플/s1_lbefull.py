def solution(s):
    answer = []
    s = s.split('},{')                              # 입력받은 문자열을
    s[0] = s[0][2:]                                 # 2차원 리스트로 만들어줌
    s[-1] = s[-1][:-2]

    for i in range(len(s)):
        s[i] = list(map(int, s[i].split(',')))      # 문자열을 정수로 변환
    s.sort(key=lambda x: len(x))                    # 리스트의 길이순서대로 정렬
    
    used = set()
    for i in range(len(s)):
        for j in range(len(s[i])):                  # 2차원 리스트를 순회
            if s[i][j] not in used:                 # 아직 나오지 않은 숫자가 있으면
                answer.append(s[i][j])              # 정답에 차례로 넣어줌
                used.add(s[i][j])
                break

    return answer
