from itertools import permutations


def solution(n, weak, dist):
    answer = len(dist) + 1    # 친구 수 초기화

    # 길이를 2배로 늘려 원형 형태를 표현
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)

    for start in range(length):
        for friend in list(permutations(dist, len(dist))):
            cnt = 1    # 점검할 친구 수
            position = weak[start] + friend[cnt-1]    # 점검한 인원의 마지막 위치

            # 모든 취약 지점 확인
            for idx in range(start, start + length):
                # 점검할 수 있는 범위를 벗어난 경우
                if position < weak[idx]:
                    cnt += 1    # 추가 인원 투입
                    if cnt > len(dist):    # 투입 인원을 초과한 경우 종료
                        break
                    position = weak[idx] + friend[cnt-1]

            answer = min(answer, cnt)    # 최솟값

    if answer > len(dist):
        return -1
    return answer