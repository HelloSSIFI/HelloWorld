"""
Greedy
아이디어 출처 : https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy
조이스틱 위, 아래 움직임 : answer 에 중첩
조이스틱 왼, 오른 움직임 : min_move 를 갱신
"""


def solution(name):
    answer = 0
    # 최소 이동값 초기값
    min_move = len(name) - 1

    for i, char in enumerate(name):
        # 조이스틱 위, 아래 움직임
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 기존 최소 이동값, 조이스틱 왼쪽 움직임, 조이스틱 오른쪽 움직임 비교 및 갱신
        min_move = min([min_move, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    # 조이스틱 왼, 오른 움직임 추가
    answer += min_move
    return answer


print(solution("JEROEN"))