def solution(commands):
    def find_set(x):                                    # 분리집합
        if x == leader[x]:                              # 대표원소를 찾는 함수
            return x                                    # x가 대표원소일 경우 x 리턴
        leader[x] = find_set(leader[x])                 # 아닐 경우 x가 가리키는 값을 넣어서 재귀하여 대표원소를 리턴
        return leader[x]


    def union_set(x, y):                                # x의 대표원소를 y의 대표원소로 바꾸는 함수
        leader[find_set(x)] = find_set(y)


    answer = []                                         # 2차원 표를 1차원으로 풀어서 진행
    table = [''] * 2601                                 # 숫자를 1부터 세므로 25 x 25 = 2601 개의 원소를 만듬
    leader = list(range(2601))                          # 대표원소도 2601개를 만들어 자신의 인덱스 번호로 초기화
    for command in commands:
        com, *info = command.split()
        if com == 'UPDATE':                             # 명령어가 UPDATE인 경우
            if len(info) == 3:                          # r c value의 형태인 경우
                r, c, value = info                      # 해당 위치의 값을 value로 바꿈
                idx = find_set(int(r) * 51 + int(c))
                table[idx] = value
            else:                                       # value1 value2 의 형태인 경우
                value1, value2 = info                   # 모든 원소를 순회하면서 value1의 값을 value2로 바꿈
                for i in range(2601):
                    if table[i] == value1:
                        table[i] = value2

        elif com == 'MERGE':                            # 명령어가 MERGE인 경우
            r1, c1, r2, c2 = map(int, info)             # 각각의 좌표를 1차원으로 바꾼 뒤
            idx1 = find_set(r1 * 51 + c1)               # 대표원소(병합된 경우)를 찾아서 idx1 idx2로 저장
            idx2 = find_set(r2 * 51 + c2)

            if idx1 == idx2:                            # 두 인덱스가 같다면 다음반복
                continue

            if table[idx1]:                             # idx1이 값을 가지고 있다면
                table[idx2] = ''                        # idx2의 값을 제거하고
                union_set(idx2, idx1)                   # idx2가 idx1 을 가리키도록 설정
            else:                                       # idx1이 비었다면
                union_set(idx1, idx2)                   # idx1이 idx2 를 가리키도록 설정

        elif com == 'UNMERGE':                          # 명령어가 UNMERGE인 경우
            r, c = map(int, info)
            idx = r * 51 + c                            # 값이 남을 칸의 인덱스를 idx
            leader_idx = find_set(idx)                  # 병합된 칸들의 대표 인덱스를 leader_idx로 저장
            for i in range(2601):                       # leader 리스트를 갱신(find_set 함수를 한번씩 실행)
                find_set(i)

            for i in range(2601):                       # 다시 leader 리스트를 순회하면서
                if leader[i] == leader_idx:             # leader_idx와 같은 값을 가지면(병합된 칸들)
                    leader[i] = i                       # 해당 칸들이 자신을 가리키도록 변경(병합 해제)

            table[idx] = table[leader_idx]              # idx에 병합중일 때의 값을 넣어주고
            if idx != leader_idx:                       # idx와 leader_idx가 다를경우
                table[leader_idx] = ''                  # leader_idx에 저장된 값을 지워줌

        else:                                           # 명령어가 PRINT인 경우
            r, c = map(int, info)
            idx = find_set(r * 51 + c)                  # 해당 칸의 대표원소를 찾아줌
            if table[idx]:                              # 값이 있다면 값을 answer에 추가해주고
                answer.append(table[idx])               # 값이 없다면 EMPTY를 추가
            else:
                answer.append('EMPTY')

    return answer


# print(solution(["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"]))
