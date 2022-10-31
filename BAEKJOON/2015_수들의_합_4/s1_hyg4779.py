# 참고: https://computer-science-student.tistory.com/660

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 합이 k인 부분합의 개수
answer = 0

# 누적합 관련 dict
sum_dict = {0: 1}

# 누적합
sum_val = 0

for i in arr:
    sum_val += i

    # 현재 누적합에서 k를 뺀 값이 dict에 있다면 answer에 해당 값의 등장 횟수를 더함
    if sum_val - k in sum_dict:
        answer += sum_dict[sum_val-k]

    # 현재 누적합 등장 횟수 추가
    if sum_val in sum_dict:
        sum_dict[sum_val] += 1

    else:
        sum_dict[sum_val] = 1

print(answer)