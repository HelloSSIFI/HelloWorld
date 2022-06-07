import math


def solution(progresses, speeds):
    answer = []
    days = list(map(lambda x, y: math.ceil((100 - x) / y), progresses, speeds))     # 개발 완료까지 남은 일 수

    day = days[0]                   # 현재 인덱스까지 가장 오래 걸리는 작업 일 수를 저장할 변수
    cnt = 0                         # 이전 배포 이후 저장된 day에서 몇 개를 배포할 수 있을지 카운트할 변수
    for i in range(len(days)):
        if days[i] <= day:          # 이전 작업보다 더 적은 일이 걸리면
            cnt += 1                # cnt +1
        else:                       # 아니라면
            answer.append(cnt)      # 현재까지 cnt를 answer에 추가 후
            day = days[i]           # 현재 날짜를 갱신
            cnt = 1                 # cnt 초기화

    answer.append(cnt)              # 반복 종료 후 남은 cnt를 answer에 넣어줌

    return answer


# print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
