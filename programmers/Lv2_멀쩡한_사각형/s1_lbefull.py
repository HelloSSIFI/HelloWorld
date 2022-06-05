def gcd(a, b):                                      # 최대 공약수 구하는 함수
    return b if a % b == 0 else gcd(b, a % b)


def solution(w, h):
    answer = w * h                          # 결과값 초기화

    if w == h:                              # 두 수가 같다면 없어지는 사각형은 w = h 개
        return answer - w

    gc = gcd(w, h)                          # 최대 공약수를 구해서
    A = min(w // gc, h // gc)               # 최대 공약수로 나눈것 까지만 확인하면
    B = max(w // gc, h // gc)               # 그 이후는 최대 공약수만큼 똑같이 반복됨

    ref_max = 0                             # 현재 행 또는 열에서 망가진 사각형의 마지막 인덱스
    ref_min = 0                             # 최초 망가진 사각형 바로 전 인덱스

    temp = 0                                # 망가진 사각형 개수
    for i in range(1, A + 1):               # 행 또는 열 중 작은 값 만큼 반복
        ref_max = (B * i) // A + 1          # A * B 가 되기 전까지는 나누어 떨어지지 않으므로 +1을 붙여줌
        if i == A:                          # i = A 가 되어 A * B 가 되면 나누어 떨어지므로 -1
            ref_max -= 1
        temp += ref_max - ref_min           # 두 인덱스의 차이가 망가진 사각형의 개수
        ref_min = (B * i) // A              # 작은 인덱스 갱신
    
    return answer - temp * gc               # 최종적으로 구한 개수 * 최대 공약수가 망가진 사각형 개수


# print(solution(8, 12))
