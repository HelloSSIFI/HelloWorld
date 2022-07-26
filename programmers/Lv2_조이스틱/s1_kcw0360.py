def solution(name):
    answer = 0
    min_move = len(name) - 1

    for i, chr in enumerate(name):
        # 현재 알파벳 변경을 위한 최소 조작 횟수 추가
        answer += min(ord(chr) - ord('A'), ord('Z') - ord(chr) + 1)

        # 현재 알파벳 이후 A 문자열 찾기
        next_idx = i + 1
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1

        # 기존 좌우 최소 움직임, 연속된 A의 왼쪽 시작, 오른쪽 시작 비교 후 최소값 갱신
        min_move = min(min_move, i + i + len(name) - next_idx, i + 2 * (len(name) - next_idx))

    # 좌우 이동 횟수 추가
    answer += min_move

    return answer