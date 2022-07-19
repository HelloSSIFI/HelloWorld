def sort_ref(x):                                    # sort 메서드의 key로 전달할 함수
    while len(x) < 9:                               # 문자열 비교를 위해
        x *= 2                                      # 현재 문자열의 길이를 가장 길 때의 2배로 맞춰줌
    x = x[:8]
    return x


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=sort_ref, reverse=True)        # 정의한 함수의 역순으로 정렬
    answer = ''.join(numbers)                       # 리스트를 다시 문자열로 합쳐줌
    if len(answer) == answer.count('0'):            # 만약 0으로만 이루어졌으면
        answer = '0'                                # 0 하나만 리턴
    return answer


# print(solution([3, 30, 34, 5, 9]))
