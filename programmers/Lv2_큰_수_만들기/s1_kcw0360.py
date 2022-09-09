def solution(number, k):
    answer = []

    for num in number:
        # num과 answer 끝 자리와 비교 후 answer의 끝이 num보다 작은 경우 지속적으로 제거
        # 이때 k값을 카운트 해주며 총 k개 이상 지울 수 없다.
        while k > 0 and answer and answer[-1] < num:
            answer.pop()
            k -= 1

        answer.append(num)    # answer에 num 추가

    return ''.join(answer[:len(answer) - k])    # 앞에서 다 지워지지 않은 경우도 있기 때문에 전체 길이에서 k를 뺀 길이 만큼 리턴