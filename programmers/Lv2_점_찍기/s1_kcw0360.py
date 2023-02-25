def solution(k, d):
    answer = 0
    length = d // k    # x 혹은 y가 0일 때 가장 멀리 떨어진 점의 좌표의 a값
    check = length * k    # a*k의 최대값

    for i in range(length+1):    # x축 방향으로 a의 값을 1씩 늘려가며 체크
        if (i*k)**2 + check**2 > d**2:    # 거리가 d보다 커지는 경우
            while (i*k)**2 + check**2 > d**2:    # k만큼 감소하면서 최대 거리가 되는 좌표 체크
                check -= k

        answer += (check//k+1)    # 해당 거리 만큼 찍히는 점 개수 추가

    return answer