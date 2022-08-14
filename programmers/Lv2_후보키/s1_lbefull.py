def comb(idx, cnt, m, relation):                        # 각 속성들의 조합을 찾아서 비교
    global answer
    if cnt == m:                                        # m개를 선택해 조합을 만들었으면
        check = set()                                   # m개의 속성들이 유일하게 식별할 수 있는지 확인할 셋
        for i in range(len(relation)):                  # 선택한 속성들을 _을 추가해 이어 붙여서
            key = ''                                    # key를 만들고
            for j in range(N):                          # 해당 key가 다시 나오는지 확인하여
                if visited[j]:                          # 유일하게 식별할 수 없다면
                    key += relation[i][j] + '_'         # 반복 종료
            if key in check:
                break
            check.add(key)
        else:                                           # 만약 유일하게 식별할 수 있다면
            key = ''                                    # 최소성을 확인
            for i in range(N):                          # 현재 선택된 속성들의 인덱스를 합쳐서 key를 만들고
                if visited[i]:                          # 이전에 후보키로 선택되었던 인덱스 key를 가져와서
                    key += str(i)                       # 해당 key 문자열을 한문자씩 반복하면서
            pos = True                                  # 모든 문자가 현재 key에 포함되어 있다면
            for k in selected:                          # 최소성을 만족하지 못하므로 추가하지 않고
                for i in range(len(k)):                 # 최소성을 만족한다면 현재 key를 selected에 추가 후
                    if k[i] not in key:                 # 결과 + 1
                        break
                else:
                    pos = False
            if pos:
                selected.add(key)
                answer += 1
        return

    for i in range(idx, N):                             # 아직 m개를 고르지 않았다면
        if not visited[i]:                              # 고르지 않은 값을 찾아
            visited[i] = 1                              # 골랐다는 표시를 해주고
            comb(i, cnt + 1, m, relation)               # 재귀 후 다시 골랐다는 표시를 지워줌
            visited[i] = 0


def solution(relation):
    global N, visited, selected, answer
    answer = 0
    N = len(relation[0])
    visited = [0] * N
    selected = set()
    for i in range(1, N + 1):
        comb(0, 0, i, relation)
    return answer


# print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
