def making(word):
    # 글자를 순회하면서 두글자 씩 대문자로 바꿔 배열에 담아 return
    if not word: return False
    return [word[i-1:i+1].upper() for i in range(1, len(word)) if word[i-1].isalpha() and word[i].isalpha()]

def solution(str1, str2):
    # str1, str2 를 각 각 making 작업
    pre = making(str1)
    post = making(str2)

    # 교집합 합집합
    cross = set(pre) & set(post)
    all = set(pre) | set(post)

    # 둘 다 공집합이라면 1*65536 return
    if not all: return 65536
    cross_val = all_val = 0

    # 교집합, 합집합을 돌며 각 개수를 취합
    for el in cross:
        cross_val += min(pre.count(el), post.count(el))

    for al in all:
        all_val += max(post.count(al), pre.count(al))

    # 결과값 리턴
    return int(cross_val/all_val*65536)