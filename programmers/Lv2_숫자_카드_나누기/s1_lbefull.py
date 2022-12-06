from math import gcd


def solution(arrayA, arrayB):
    answer = 0
    n1 = arrayA[0]
    n2 = arrayB[0]
    for i in range(1, len(arrayA)):         # 각각 두 배열의 최대공약수를 구해줌
        n1 = gcd(n1, arrayA[i])             # 만약 A배열의 최대공약수 n1이 B배열에서 나누어 떨어진다면
        n2 = gcd(n2, arrayB[i])             # n1보다 작은 공약수들도 어차피 나누어 떨어지므로 최대공약수만 비교
        
    for i in arrayA:
        if i % n2 == 0:                     # 각각 최대공약수를 다른 배열의 요소와 비교하여
            n2 = 0                          # 나누어 떨어지면 0으로 바꿔줌
            break

    for i in arrayB:
        if i % n1 == 0:
            n1 = 0
            break

    answer = max(n1, n2)                    # 최대값 출력
    return answer


# print(solution([10, 17], [5, 20]))
