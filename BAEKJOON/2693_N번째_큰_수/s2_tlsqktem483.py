def quick_sort(array):
    # 리스트가 하나 이하의 원소를 가지면 종료
    if len(array) <= 1: return array

    pivot, tail = array[0], array[1:]

    leftSide = [x for x in tail if x <= pivot]
    rightSide = [x for x in tail if x > pivot]

    return quick_sort(leftSide) + [pivot] + quick_sort(rightSide)

T = int(input())

for tc in range(1, T+1):
    A = list(map(int, input().split()))
    print(quick_sort(A)[-3])