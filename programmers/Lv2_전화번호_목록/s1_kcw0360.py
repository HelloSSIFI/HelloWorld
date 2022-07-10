def solution(phone_book):
    answer = True
    phone_book.sort()   # key 값을 길이로 주어 길이순으로 정렬

    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return answer