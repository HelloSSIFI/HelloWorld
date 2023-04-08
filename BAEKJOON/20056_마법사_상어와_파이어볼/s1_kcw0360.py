from collections import defaultdict
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

fireball = defaultdict(list)    # (행, 열): [[질량, 속력, 방향]]

for _ in range(m):
    # [행, 열, 질량, 속력, 방향]
    temp = list(map(int, input().split()))
    fireball[(temp[0]-1, temp[1]-1)].append(temp[2:])

#방향
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(k):    # 명령 횟수 만큼 반복
    temp = defaultdict(list)    # 이동한 파이어볼 정보 저장

    # 숫자는 문제에서 주어진 조건
    # 1
    for key, val in fireball.items():
        for info in val:
            y = (key[0] + info[1] * dy[info[2]]) % n
            x = (key[1] + info[1] * dx[info[2]]) % n
            temp[(y, x)].append(info)

    # 2
    for key, val in temp.items():
        num = len(val)    # 좌표에 있는 파이어볼 수
        if num >= 2:    # 좌표에 파이어볼이 하나 있다면 2번 조건 pass
            mass, speed, a, b = 0, 0, 0, 0    # 누적 질량, 누적 속력, 홀수 방향 개수, 짝수 방향 개수
            for info in val:
                mass += info[0]
                speed += info[1]
                if info[2] % 2:
                    a += 1
                else:
                    b += 1

            mass //= 5    # 2.3.1
            speed //= num    # 2.3.2

            if mass:    # 2.3.3
                if a == num or b == num:    # 모두 홀수 or 모두 짝수인 경우
                    temp[key] = [[mass, speed, 0], [mass, speed, 2], [mass, speed, 4], [mass, speed, 6]]
                else:    # 나머지
                    temp[key] = [[mass, speed, 1], [mass, speed, 3], [mass, speed, 5], [mass, speed, 7]]
            else:    # 2.4
                temp[key] = []

    fireball = temp

answer = 0
for val in fireball.values():    # 질량의 합
    for info in val:
        answer += info[0]

print(answer)