'''
https://leedakyeong.tistory.com/entry/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%A9%80%EC%A9%A1%ED%95%9C-%EC%82%AC%EA%B0%81%ED%98%95-in-python
'''


def solution(w, h):

    a = w           # W와 H의 GCD를 찾기위한 변수
    b = h

    while b > 0:
        a, b = b, a % b

    return w * h - (w + h - a)      # 총 사각형 개수 - (가로길이 + 세로길이 - 최대공약수)