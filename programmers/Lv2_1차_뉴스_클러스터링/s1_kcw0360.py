def change(word):
    # 대소문자 구분이 없다고 했으므로 하나로 통일해주기(소문자)
    word = word.lower()
    temp = []

    # 연속된 두개의 글자가 문자면 원소로 넣기
    for i in range(len(word)-1):
        if word[i:i+2].isalpha():
            temp.append(word[i:i+2])

    return temp


def solution(str1, str2):
    answer = 1

    # 입력받은 문자열을 두 글자씩 끊어서 집합 만들기
    word1 = change(str1)
    word2 = change(str2)

    # 공집합 제거
    if word1 == [] and word2 == []:
        return answer * 65536

    # 교집합 구하기
    intersection = []
    for i in word1:
        if i in word2:
            intersection.append(i)
            word2.remove(i)

    # 합집합 구하기
    union = word1 + word2

    # 유사도 구하기
    answer = int(len(intersection)/len(union)*65536)

    return answer