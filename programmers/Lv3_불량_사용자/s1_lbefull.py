def solution(user_id, banned_id):


    def dfs(cnt):                                       # 제재 가능한 아이디 목록들로 조합을 만듬
        if cnt == M:                                    # M개를 골랐다면
            sorted_sel = sorted(selected)               # 정렬 후 _를 이용해 이어붙임
            sorted_sel = '_'.join(sorted_sel)           # 해당 단어가 한번도 안나온 단어이면
            if sorted_sel not in answer:                # 결과 set에 추가
                answer.add(sorted_sel)
            return

        for name in candi[cnt]:                         # 아직 고르지 않았다면
            if not visited[name]:                       # 현재 골라야하는 인덱스의 후보군을 탐색
                visited[name] = 1                       # 다른 인덱스 후보군에서 고르지 않았다면
                selected.append(name)                   # 고름 표시 후 선택 리스트에 추가
                dfs(cnt + 1)                            # 재귀 후 다시 표시를 제거하고 리스트에서 삭제
                selected.pop()
                visited[name] = 0


    answer = set()
    N = len(user_id)
    M = len(banned_id)
    candi = [[] for _ in range(M)]                                  # 각 banned_id에 선택될 수 있는 user_id를 리스트 형태로 저장
    visited = dict()                                                # 조합을 만들 때 골랐는지 판별할 딕셔너리
    selected = []                                                   # 조합을 만들 때 고른 아이디를 넣어줄 리스트
    for i in range(N):                                              # 딕셔너리 초기화
        visited[user_id[i]] = 0
    
    for i in range(M):
        for j in range(N):
            if len(banned_id[i]) != len(user_id[j]):                # 불량 사용자 아이디 길이와 유저 아이디 길이가 다를경우
                continue                                            # 다음반복
            for k in range(len(banned_id[i])):                      # 길이가 같을 경우, 한 글자씩 보면서
                if banned_id[i][k] not in (user_id[j][k], '*'):     # 서로 같거나 *인경우는 통과 아닐경우 반복종료
                    break
            else:                                                   # 모든 문자가 일치할 경우
                candi[i].append(user_id[j])                         # 후보군의 인덱스에 맞게 추가
    dfs(0)
    return len(answer)


# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))
