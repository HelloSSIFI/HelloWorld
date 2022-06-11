N, S = map(int, input().split())        # N개 숫자, 목표치 S
arr = list(map(int, input().split()))   # N개 숫자 배열


# for i in range(1, N+1):
#
#     for j in range(N-i+1):
#         tmp = sum(arr[j:j+i])
#
#         if tmp >= S:
#             print(i)
#             exit()

left, right = 0, 0                      # 좌 우 포인터
tmp = 0                                 # 임시 sum 값
result = N+1                            # 길이 최댓값

while True:                             # right != N 시 틀림
    if tmp >= S:                        # sum이 목표치 이상 시
        result = min(result, right - left)  # 길이 최솟값 갱신
        tmp -= arr[left]                    # 왼쪽을 한 칸 줄임
        left += 1

    elif right == N:                        # 끝까지 돌았다면 멈춤
        break

    else:                                   # 값이 S가 안 됐다면 오른 쪽으로 한 칸 넓힘
        tmp += arr[right]
        right += 1

if result == N+1:
    print(0)
else:
    print(result)