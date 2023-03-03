def solution(routes):
    routes.sort(key=lambda x: x[1])                 # 종료시간 기준 오름차순 정렬

    answer = 0
    prev = -40000                                   # 이전 종료시간을 저장할 변수
    for i in range(len(routes)):                    # 모든 차량 경로 확인
        if prev < routes[i][0]:                     # 이전 카메라를 만난 차량들 중 가장 큰 진출 좌표보다
            prev = routes[i][1]                     # 현재 차량 진입 좌표가 크다면, 현재 차량의 진출지점으로 prev를 갱신하고
            answer += 1                             # answer +1

    return answer


# print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
