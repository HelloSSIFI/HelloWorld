def convert(num, n):    # 10진수를 n진수로 변환하는 함수
    check = "0123456789ABCDEF"
    a, b = divmod(num, n)
    if a == 0:
        return check[b]
    else:
        return convert(a, n) + check[b]


def solution(n, t, m, p):    # n: 진법, t: 미리 구할 숫자의 갯수, m: 참가 인원, p: 튜브의 순서
    answer = ''    # 튜브의 숫자만 저장
    result = ''    # 0부터 변환한 모든 수를 저장
    num = 0    # 변환하려는 수 초기화
    while len(result) <= t*m:    # 필요한 개수 만큼 반복
        result += convert(num, n)  # 해당 숫자 변환 후 result에 추가
        num += 1    # 다음 숫자

    for idx in range(p-1, len(result), m):    # 튜브 순서의 값만 answer에 추가
        answer += result[idx]
        if len(answer) == t:    # 미리 구할 숫자의 갯수가 충족한 경우 반복문 빠져나가기
            break

    return answer