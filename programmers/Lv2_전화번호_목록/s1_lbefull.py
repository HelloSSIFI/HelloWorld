def solution(phone_book):
    used = set()
    phone_book.sort(key=lambda x: len(x))                   # 전화번호를 길이순서로 정렬
    for i in range(len(phone_book)):
        for j in range(1, len(phone_book[i]) + 1):          # 전화번호의 앞부분부터 차례로 잘라서
            if phone_book[i][:j] in used:                   # 앞에 나온 전화번호화 일치하는게 있다면
                return False                                # False 리턴
        used.add(phone_book[i])                             # 없다면 현재 전화번호를 used에 추가
    return True

# print(solution(["119", "97674223", "1195524421"]))
