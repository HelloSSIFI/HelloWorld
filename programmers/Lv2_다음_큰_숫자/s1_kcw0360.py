def solution(n):
    cnt = bin(n)[2:].count("1")
    for answer in range(n+1, 1000001):
        if cnt == bin(answer)[2:].count("1"):
            return answer