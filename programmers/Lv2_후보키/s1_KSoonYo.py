
def check_uniq(cnt, i, attributes, temp_cnt, temp_set, candidates, relations):
    if temp_cnt == cnt:
        values = []
        for relation in relations:
            # 유일성 체크
            # attribute에 따라 들어가는 순서가 달라도 다른 값이므로 이를 구분하기 위해 set 대신 list를 써야 함
            # 즉 ['a', 'aa'] 와 ['aa', 'a'] 는 다른 값의 조합이지만 set으로 하면 모두 같아지므로 유일성 체크에 오류가 생김
            temp = []
            for attr in temp_set:
                temp.append(relation[attr])
            if temp in values:
                return
            values.append(temp)
        
        # 유일성 체크 완료했다면
        # 최소성 체크
        # 현재의 키 조합이 후보키에 있는 조합을 포함한다면 return
        for candidate in candidates:
            if temp_set >= candidate:
                return
        candidates.append(temp_set)
        return 

    for idx in range(i, len(attributes)):
        temp_set.add(attributes[idx])
        check_uniq(cnt, idx + 1, attributes, temp_cnt + 1, temp_set.copy(), candidates, relations)
        temp_set.remove(attributes[idx])



def solution(relation):
    answer = 0
    attributes = [i for i in range(len(relation[0]))]

    candidates = []

    for cnt in range(1, len(relation[0]) + 1):
        check_uniq(cnt, 0, attributes, 0, set(), candidates, relation)

    answer = len(candidates)
    return answer


# solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]])
# solution([["100","100","ryan","music","2"], ["200","200","apeach","math","2"], ["300","300","tube","computer","3"], ["400","400","con","computer","4"], ["500","500","muzi","music","3"], ["600","600","apeach","music","2"]])
# solution([['a', '1', 'aaa', 'c', 'ng'], ['a', '1', 'bbb', 'e', 'g'], ['c', '1', 'aaa', 'd', 'ng'], ['d', '2', 'bbb', 'd', 'ng']])
solution([['a', 'aa'], ['aa', 'a'], ['a', 'a']]) # -> 주의 케이스
