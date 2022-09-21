import sys
input = sys.stdin.readline


N = int(input())
solution = list(map(int, input().split()))
solution.sort()    # 알칼리성과 산성을 구분하기 위해 정렬
alkaline = 0    # 알칼리성의 시작idx
acid = len(solution) - 1    # 산성의 시작 idx
result = abs(solution[alkaline] + solution[acid])    # 초기 각 특성 용액의 idx에 위치한 용액의 특성값

answer = [0, 0]    # [알칼리성, 산성]
while alkaline < acid:    # 알칼리성 idx가 산성 idx가 되기 전까지 반복
    mix = solution[alkaline] + solution[acid]    # 섞은 용액의 특성값

    if abs(mix) <= result:    # 특성값이 0에 더 가까운 경우
        result = abs(mix)    # 현재값을 result 값으로 대체
        answer = [solution[alkaline], solution[acid]]

        if result == 0:    # 특성값이 0이 되는 경우 더 이상 확인할 필요가 없으므로 반복문 빠져나오기
            break

    if mix < 0:    # 섞은 용액의 특성값의 알칼리성이 산성용액보다 큰 경우
        alkaline += 1    # 알칼리성 idx 이동
    else:    # 반대의 경우
        acid -= 1    # 산성 idx 이동

print(*answer)
