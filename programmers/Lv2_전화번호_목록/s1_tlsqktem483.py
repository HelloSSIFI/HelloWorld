def solution(phone_book):
    phone_book = sorted(phone_book)

    print(*zip(phone_book, phone_book[1:]))
    for p1, p2 in zip(phone_book, phone_book[1:]):
        print(p1, p2)
        if p2.startswith(p1):
            return False
    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))