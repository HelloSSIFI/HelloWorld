'''
1. 입력된 수가 짝수라면 2로 나눔
2. 입력된 수가 홀수라면 3곱하고 1을 더함
3. 결과로 나온 수가 1보다 크다면 1번 작업을 반복

'''

def solution(k, ranges):
    answer = []
    area = []

    # k가 1이 될 때까지 밑변 1씩 면적값 입력
    while k > 1:
        if k%2:
            new = k*3 + 1
            area.append(k+(new-k)/2)
        else:
            new = k/2
            area.append(new + (k-new)/2)
        k = new

    # x의 끝값
    x = len(area)

    # 정적분
    for s, e in ranges:
        e += x
        if s <= e:
            answer.append(sum(area[s:e]))
        else:
            answer.append(-1)

    print(answer)
    return answer

solution(5, [[0, 0], [0, -1], [2, -3], [3, -3]])
