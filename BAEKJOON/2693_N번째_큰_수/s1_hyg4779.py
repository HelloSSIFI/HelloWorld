def q_sort(args):
    if len(args) <= 1:
        return args

    pivot = args[0]             # 기준 피벗: 배열의 첫번째 위치
    tail = args[1:]             # 피벗을 제외한 나머지 배열

    left = [x for x in tail if x <= pivot]       # 피벗 보다 작은 숫자들
    right = [x for x in tail if x > pivot]       # 피벗 보다 큰 숫자들

    return q_sort(left) + [pivot] + q_sort(right)


arr = [list(map(int, input().split())) for _ in range(int(input()))]

for x in range(len(arr)):
    tmp = q_sort(arr[x])
    print(tmp[-3])