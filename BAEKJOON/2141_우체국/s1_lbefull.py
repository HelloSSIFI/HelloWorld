import sys
input = sys.stdin.readline


N = int(input())
people = []
ls = rs = 0                                                 # 인덱스 기준 왼쪽의 숫자합을 ls, 오른쪽 합을 rs로 저장
for i in range(N):                                          # 인덱스는 왼쪽부터 탐색할 예정이므로 초기 오른쪽 합은 총 인구합과 같음
    people.append(list(map(int, input().split())))          # 마을 위치별로 오름차순 정렬
    rs += people[i][1]
people.sort()

answer = 0
for i in range(N):                                          # 마을 기준으로 오른쪽에 우체국을 지을수록
    if ls >= rs:                                            # 우체국이 지어지는 마을 포함 오른쪽 사람들은 왼쪽으로부터 이동한 거리만큼 이득을 보고
        break                                               # 우체국을 포함하지 않은 왼쪽 사람들은 이동한 거리만큼 손해를 봄
    answer = people[i][0]                                   # 따라서 왼쪽 사람 수가 커지기 직전까지 오른쪽으로 이동하면 됨
    ls += people[i][1]
    rs -= people[i][1]

print(answer)
