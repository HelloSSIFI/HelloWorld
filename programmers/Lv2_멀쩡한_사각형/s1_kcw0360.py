import math
def solution(w,h):
    num = math.gcd(w, h)

    answer = (w*h) - (w+h-num)

    return answer