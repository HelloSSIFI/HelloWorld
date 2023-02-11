from itertools import product


def solution(users, emoticons):
    answer = []
    sales = [10, 20, 30, 40]    # 이모티콘의 할인율

    for case in product(sales, repeat=len(emoticons)):    # 이모티콘마다 할인율을 적용하는 모든 경우를 체크
        result = [0, 0]
        for user in users:    # 유저마다 이모티콘 구매 후 가격 체크
            temp = 0    # user의 이모티콘 구입 지불 비용
            for idx, sale in enumerate(case):
                if sale >= user[0]:    # 이모티콘 할인율이 유저가 원하는 할인율 이상이면 구매
                    temp += emoticons[idx] * (100 - sale) // 100

            if temp >= user[1]:    # 유저가 생각하는 예산보다 초과하는 경우 이모티콘 플러스에 가입
                result[0] += 1    # result에 이모티콘 플러스 가입자 카운트 +1
            else:
                result[1] += temp    # 이모티콘 플러스에 가입하지 않는다면 result에 이모티콘 구매 가격 누적

        answer.append(result)    # 해당 할인율 경우에서 구한 결과값을 answer에 추가

    answer.sort(key=lambda x: (-x[0], -x[1]))    # 이모티콘 플러스 가입자 최대(우선순위), 이모티콘 판매액 최대로 정렬

    return answer[0]