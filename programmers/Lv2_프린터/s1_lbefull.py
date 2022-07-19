def solution(priorities, location):
    answer = 0
    while True:
        n = priorities.pop(0)                               # 인쇄목록의 제일 앞 문서를 꺼냄
        if not priorities or n >= max(priorities):          # 다른 문서보다 우선순위가 높거나 같으면
            answer += 1                                     # 출력횟수 + 1
            if location == 0:                               # 만약 내가 요청한 문서이면
                return answer                               # 반환
        else:                                               # 우선순위가 낮다면
            priorities.append(n)                            # 마지막에 넣어줌
        location = (location -1) % len(priorities)          # 인덱스 조정


# print(solution([2, 1, 3, 2], 2))
