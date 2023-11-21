import math

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = answer * arr[i] // math.gcd(answer, arr[i])

    return answer