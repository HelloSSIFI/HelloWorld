def solution(phone_book):
    answer = True
    phone_book.sort()   # 길이 순으로 정렬

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):    # 현재 번호가 다음 번호에 접두어 인지 체크
            return False                                 # 바로 뒤에 포함이 안된다면 그 이후 번호에도 포함이 되지 않기 때문(길이순으로 정렬한 것이기 때문)

    return answer