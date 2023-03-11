def solution(routes):
    answer = 0
    routes.sort(key=lambda x: x[1])    # 진출 기준으로 정렬
    cam = -30001    # 카메라 설치 위치(초기화)

    for i in range(len(routes)):
        if cam < routes[i][0]:    # 카메라 위치 값이 진입한 차량 위치 값 보다 작은 경우
            answer += 1    # 카메라 추가 설치
            cam = routes[i][1]    # 카메라 설치 위치 갱신

    return answer