def check(answer):
    for x, y, a in answer:
        if a:    # 보인 경우
            if [x, y-1, 0] not in answer and [x+1, y-1, 0] not in answer and \
                    not ([x-1, y, 1] in answer and [x+1, y, 1] in answer):
                return True
        else:    # 기둥인 경우
            if y != 0 and [x, y-1, 0] not in answer and [x, y, 1] not in answer and [x-1, y, 1] not in answer:
                return True
    return False


def solution(n, build_frame):
    answer = []

    for x, y, a, b in build_frame:
        if b:    # 구조물 설치
            answer.append([x, y, a])
            if check(answer):
                answer.remove([x, y, a])
        else:    # 구조물 삭제
            answer.remove([x, y, a])
            if check(answer):
                answer.append([x, y, a])
    answer.sort()
    return answer