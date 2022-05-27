
def case1(numbers_list, k = 3):
    # 역순으로 정렬한 뒤 k-1번째 원소를 출력

    sorted_list = sorted(numbers_list, reverse=True)
    return sorted_list[k-1]

def case2(numbers_list, k = 3):
    # K번째 큰 값을 찾는 알고리즘(k가 작을 때 유용)
    for i in range(0, k):
        max_index = i
        for j in range(i+1, len(numbers_list)):
            if numbers_list[max_index] < numbers_list[j]:
                max_index = j
        numbers_list[i], numbers_list[max_index] = numbers_list[max_index], numbers_list[i]

    return numbers_list[k-1]

# Quick Selection 알고리즘
# def quick_selection(numbers_list, start, end, k = 3):

#     mid = (start + end) // 2
#     pivot = numbers_list[mid]
#     left_idx = start
#     right_idx = end

#     # swap
#     while left_idx < right_idx:
#         if numbers_list[left_idx] > pivot:
#             left_idx += 1
#             continue

#         if numbers_list[right_idx] < pivot: 
#             right_idx -= 1
#             continue

#         numbers_list[left_idx], numbers_list[right_idx] = numbers_list[right_idx], numbers_list[left_idx]

#     if k - 1 == mid:
#         return numbers_list[mid]
#     elif k - 1 > mid:
#         return quick_selection(numbers_list, mid + 1, end)
#     elif k - 1 < mid:
#         return quick_selection(numbers_list, start, mid - 1)

# https://debuglog.tistory.com/70

def quick_selection(arr, kth):
    pivot = arr[(len(arr) + 1) // 2 - 1]
    left, mid, right = [], [], []
    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] > pivot:
            right.append(arr[i])
        else:
            mid.append(arr[i])
    
    if kth < len(left):
        return quick_selection(left, kth)
    elif kth < len(left) + len(mid):
        return mid[0]
    else:
        return quick_selection(right, kth - len(left) - len(mid))

for test in range(int(input())):
    numbers_list = list(map(int, input().split()))
    # print(case1(numbers_list))
    # print(case2(numbers_list[:]))
    print(quick_selection(numbers_list, 7))
