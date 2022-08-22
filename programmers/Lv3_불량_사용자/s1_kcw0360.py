from itertools import permutations


def check(user_list, ban_list):
    for i in range(len(user_list)):
        if len(user_list[i]) != len(ban_list[i]):    # id 길이가 다를 경우 False
            return False
        for j in range(len(user_list[i])):
            if ban_list[i][j] == '*':    # 가려진 부분은 pass
                continue
            if user_list[i][j] != ban_list[i][j]:    # 글자가 다른 경우 False
                return False
    return True    # 모두 통과한 경우 True


def solution(user_id, banned_id):
    answer = []
    for pmt in permutations(user_id, len(banned_id)):    # 제재 아이디 수에 맞게 user_id 순열 생성
        if check(pmt, banned_id):    # 제재 아이디 인지 확인
            pmt = set(pmt)    # 제재 아이디가 맞는 경우 해당 순열을 set으로 만들기(answer에서 확인시 원소는 같고 순서만 다른 중복을 피하기 위함)
            if pmt not in answer:    # answer에 없는경우 추가
                answer.append(pmt)

    return len(answer)