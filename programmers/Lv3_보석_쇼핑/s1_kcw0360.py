def solution(gems):
    answer = [0, len(gems)-1]    # 최대 길이 일때로 초기값 설정
    gems_num = len(set(gems))    # 보석 종류의 수
    gems_type = dict()    # 보석 체크를 위한 dict
    left = 0    # 좌측 포인터
    right = 0    # 우측 포인터
    answer_len = 100000    # 최대값(제한사항)
    gems_type[gems[0]] = 1    # 시작 값 넣어주기

    while left < len(gems) and right < len(gems):    # 두 포인터가 마지막에 도달 했을 때 종료
        if len(gems_type) == gems_num:    # 모든 종류가 모였을 때
            temp = right - left    # 배열 길이 측정

            if answer_len > temp:    # temp 값이 작다면 값을 바꿔준 후 answer의 좌표도 교체
                answer_len = temp
                answer = [left+1, right+1]    # 출력 값은 1부터 시작이기 때문에 +1

            if gems_type[gems[left]] == 1:    # 현재 좌측 포인터에 해당하는 idx에 값이 dict에 존재하는 경우
                del gems_type[gems[left]]    # 하나만 존재 한다면 dict에서 삭제
            else:
                gems_type[gems[left]] -= 1    # 그 이상이면 하나만 차감

            left += 1    # 포인터 이동

        else:
            right += 1    # 모든 종류가 모이지 않았다면 우측 포인터를 이동

            if right < len(gems):    # 우측 포인터가 입력길이를 넘어서지 않아야함
                if gems[right] in gems_type:    # 이미 dict에 포함되어 있다면 +1, 아닌 경우 종류 자체를 dict에 추가
                    gems_type[gems[right]] += 1
                else:
                    gems_type[gems[right]] = 1

    return answer