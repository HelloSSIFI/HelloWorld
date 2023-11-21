def solution(prices):
    length = len(prices)
    answer = [0] * length
    # 완전탐색을 이용한 풀이
    for i in range(length-1):    # 마지막 시점의 주식은 다음 가격이 없기 때문에 떨어지지 않으므로 무조건 0
        for j in range(i, length-1):    # 현 시점(i)부터 이후 시점 모두 체크
            if prices[i] <= prices[j]:    # 현 시점(i)의 주식 가격 기준보다 떨어지지 않는 다면 +1초
                answer[i] += 1
            else:    # 떨어지는 경우 해당 위치에서 더 이상 체크 x
                break

    return answer