def solution(str1, str2):
    answer = 1
    str1_dict = dict()
    str2_dict = dict()
    for i in range(len(str1) - 1):                          # str1에서 2글자씩 자르면서 모두 알파벳이면
        if str1[i].isalpha() and str1[i + 1].isalpha():     # 딕셔너리에 해당 글자 카운트+1
            str1_dict[(str1[i] + str1[i + 1]).lower()] = str1_dict.get((str1[i] + str1[i + 1]).lower(), 0) + 1
    
    for i in range(len(str2) - 1):                          # str1과 마찬가지
        if str2[i].isalpha() and str2[i + 1].isalpha():
            str2_dict[(str2[i] + str2[i + 1]).lower()] = str2_dict.get((str2[i] + str2[i + 1]).lower(), 0) + 1
    
    key_set = set()                                         # 두 딕셔너리의 key를 모두 모아 key_set에 담아줌
    key_set.update(str1_dict)
    key_set.update(str2_dict)

    intersection = dict()                                   # 두 딕셔너리 중 작은 값을 넣어주면 교집합
    union = dict()                                          # 두 딕셔너리 중 큰 값을 넣어주면 합집합
    for key in key_set:
        union[key] = max(str1_dict.get(key, 0), str2_dict.get(key, 0))
        intersection[key] = min(str1_dict.get(key, 0), str2_dict.get(key, 0))
    
    if len(union):                                          # 합집합이 0이 아니라면 유사도를 구해줌
        answer = sum(intersection.values()) / sum(union.values())

    return int(answer * 65536)
