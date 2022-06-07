def gcd(a, b):
    return b if a % b == 0 else gcd(b, a % b)


def solution(w, h):                 # 선은 항상 가로선을 지나거나 세로선을 지날때마다 하나의 사각형을 망가뜨림 (기본적으로 망가지는 사각형 = w + h)
    whole = w * h                   # 두 선이 교차하는 지점을 지나면 두개의 사각형이 아닌 하나의 사각형을 망가뜨리므로
    broken = w + h - gcd(w, h)      # 두 선이 교차하는 지점(=최대 공약수) 만큼 다시 복구
    return whole - broken
