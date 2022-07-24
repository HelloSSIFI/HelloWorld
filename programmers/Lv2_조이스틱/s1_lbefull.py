from collections import deque


def solution(name):
    Q = deque()
    Q.append((0, 0, 'A' * len(name)))                           # Q에 인덱스, 횟수, 환성된 문자를 넣어줌
    while Q:
        p, cnt, n = Q.popleft()                                 # 횟수에 위키, 아래키 중 횟수가 적은쪽을 더해줌
        cnt += min((ord(n[p]) - ord(name[p])) % 26, (ord(name[p]) - ord(n[p])) % 26)
        n = n[:p] + name[p] + n[p + 1:]                         # 현재 위치에 완성된 문자를 바꿔줌
        if n == name:                                           # name과 같을 경우 반복 종료
            break

        Q.append(((p + 1) % len(name), cnt + 1, n))             # 아닐경우 왼쪽과 오른쪽으로 모두 이동
        Q.append(((p - 1) % len(name), cnt + 1, n))
    return cnt


# print(solution('JEROEN'))
