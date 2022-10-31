def change_sec(time):    # 시간을 초로 변환하는 함수
    h, m, s = map(int, time.split(':'))
    return h * 3600 + m * 60 + s


def solution(play_time, adv_time, logs):
    answer = 0
    arr = [0] * (change_sec(play_time) + 1)    # 전체 상영 시간을 초 단위로 구분한 arr 생성(해당 시간에 상영중인 인원 추가)

    for log in logs:
        start, end = log.split('-')    # 시작시간, 종료시간
        arr[change_sec(start)] += 1    # 시청 시작 인원
        arr[change_sec(end)] -= 1    # 시청 종료 인원

    arr_sum = [0, arr[0]]    # 해당 재생 시간 누적 인원
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]    # 해당 시간에 시청하고 있는 인원 구하기(누적)
        arr_sum.append(arr_sum[-1]+arr[i])    # 해당 재생 시간 누적 인원

    ad = change_sec(adv_time)    # 광고 시간 초로 변환

    mt = 0
    for i in range(len(arr)):
        if i + 1 + ad >= len(arr):    # 현재 시간(i)부터 광고가 끝나는 시간이 총 상영 시간보다 높은 경우 광고 삽입 불가
            break    # 그 이후 시간은 확인 불필요하기 때문에 반복문 빠져나가기

        temp = arr_sum[i+ad] - arr_sum[i]    # 해당 시간사이의 누적 시청 인원 (광고 누적 재생 시간)

        if temp > mt:
            mt = temp
            answer = i

    # 초를 시간:분:초로 변환 후 출력 규칙에 맞게 변환
    ah, answer = divmod(answer, 3600)
    am, answer = divmod(answer, 60)
    print(arr_sum)
    return '{}:{}:{}'.format(str(ah).zfill(2), str(am).zfill(2), str(answer).zfill(2))