def solution(phone_book):
    answer = True
    phone_book.sort()                                           # ['12' , '3422', '12344' , '1322'] -> ['12', '12344', '1322', '3422'] 정렬
    
    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]):         # 이미 정렬되어 있으므로 i번째 전화번호가 i + 1번째 번호의 접두어인지만 판별하면 ok
            return False
    return answer