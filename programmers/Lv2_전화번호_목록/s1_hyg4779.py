# 첫 풀이 / 효율성 테스트 3,4 시간초과
# def solution(phone_book):
#
#     for i in range(len(phone_book)):
#
#         for j in range(len(phone_book)):
#             if i==j:continue
#             if phone_book[i].find(phone_book[j])==0:
#                 return False
#
#
#     return True


def solution(phoneBook):
    print(phoneBook)

    phoneBook = sorted(phoneBook)

    print(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

solution(["119", "97674223", "1195524421"])
solution(["123", "456", "789"])
solution(["12", "123", "1235", "567", "88"])