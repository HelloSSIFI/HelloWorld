def solution(storey):
    answer = 0
    storey = list(map(int, str(storey)))    # 숫자를 각 자리수로 나누어 체크 하기 위한 리스트
    now = len(storey) - 1    # 1의 자리가 되는 지점의 idx

    while now >= 0:
        if storey[now] <= 4:    # 해당 자리의 수가 0 ~ 4인 경우 엘리베이터는 내려가는 것이 돌 소모가 적다
            answer += storey[now]    # 내려간 만큼 answer에 사용한 돌의 개수 추가

        elif 6 <= storey[now]:    # 해당 자리의 수가 6 ~ 9인 경우 올라가는 것이 돌 소모가 적다.
            answer += 10 - storey[now]    # 올라간 만큼 answer에 사용한 돌의 개수 추가

            if now == 0:    # 엘리베이터가 올라갔지만 입력받은 값에서 올림이 필요한 경우
                answer += 1    # +1
            else:    # 아닌 경우 다음 idx의 값에 엘리베이터가 올라갔으므로 해당 층의 자리의 수 +1
                storey[now-1] += 1

        else:    # 해당 자리의 수가 5인 경우
            flag = True
            temp = now    # temp는 now의 다음 자리수를 체크하기위한 임시값
            # 입력값의 길이가 2이상인 조건을 추가한 이유는 5로만 구성된 층수일 때, 5층에서는 내려가는 것이 빠르지만
            # 입력받은 층수가 2자리수 이상인  경우에는 올라갔다가 한번에 내려가는 것이 돌 소모가 적기 때문이다.
            while temp >= 0 and len(storey) >= 2:
                # 5와 다른 수가 나온다면 반복문을 빠져나간다.
                if storey[temp] <= 4:
                    flag = False    # 4이하인 경우에는 내려가는 것이 좋다.
                    break
                elif 6 <= storey[temp]:
                    break

                temp -= 1    # 자리수 이동

            if flag:    # 5 다음으로 오는 수가 6이상인 경우
                storey[now-1] += 1    # 엘리베이터가 올라가기 때문에 다음 자리수의 값 +1

            answer += 5    # 사용 돌 개수 추가

        now -= 1    # 다음 자리의 값을 체크하기 위해 idx 이동

    return answer