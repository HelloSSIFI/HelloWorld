def solution(n):
    ans = 0
    while n != 0:
        n, b = divmod(n, 2)
        ans += b

    return ans

# 해당 방식을 이진법을 이용하면 간결하게 표현할 수 있다는 것을 알게 되었고 코드는 다음과 같다.
# def solution(n):
#     return bin(n).count("1")
