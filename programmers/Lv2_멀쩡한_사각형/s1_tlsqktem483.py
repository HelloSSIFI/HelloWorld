import math
"""
최대공약수 풀이
겹치는 사각형 : 가로 세로의 최대 공약수
"""
def solution(w,h):
    g = math.gcd(w,h)
    return w*h - (w+h-g)