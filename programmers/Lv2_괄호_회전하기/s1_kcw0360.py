from collections import deque

def solution(s):
    answer = 0

    if len(s) % 2:    # 길이가 홀수인 경우 무조건 0
        return 0
    else:
        temp = deque(s)
        for i in range(len(s)):    # 전체 길이를 돌며 확인
            temp.rotate(1)    # 한 칸 이동(0 1 2 3 => 1 2 3 0)
            s = ''.join(temp)    # 이동한 것을 다시 문자열로 변환
            # 완성된 괄호 없애기
            while '[]' in s or '()' in s or '{}' in s:
                if '[]' in s:
                    s = s.replace('[]', '')
                if '()' in s:
                    s = s.replace('()', '')
                if '{}' in s:
                    s = s.replace('{}', '')

            if s == '':    # 모두 없어졌다면 +1
                answer += 1

        return answer