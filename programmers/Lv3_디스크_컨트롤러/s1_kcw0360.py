def solution(jobs):
    answer = 0
    jobs.sort(key=lambda x: x[1])   # 작업 소요 시간 으로 정렬 / 짧은 작업 시간을 먼저 끝내는 것이 좋다.
    temp = 0    # 현재 작업 중인 시간
    jobs_len = len(jobs)    # 작업 수

    while len(jobs):    # 작업 반복
        cp = 987654321    # 중간에 빈 공간이 있다면 한번에 뛰어 넘기 위한 checkpoint
        for i in range(len(jobs)):
            if jobs[i][0] <= temp:    # 작업 요청 시간이 현재 작업 중인 시간보다 같거나 선행되는 경우
                temp += jobs[i][1]    # 현재 작업 시간 + 작업 소요 시간
                answer += (temp - jobs[i][0])    # 요청 시간 이후 대기 시간 + 작업 시간
                jobs.pop(i)    #  현 작업 제거
                break    #
            elif cp > jobs[i][0]:    # 작업 요청시간이 현 시각보다 나중인 경우(그 중에서도 가장 빠른 부분을 체크)
                cp = jobs[i][0]    # cp에 지점 저장

            if i == len(jobs) - 1:    # 반복문을 완료했는데도 작업이 이루어지지 않는 경우
                temp = cp    # checkpoint로 넘어가 다음 작업을 수행할 수 있도록 한다.

    return answer // jobs_len