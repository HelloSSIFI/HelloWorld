for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)      # 내림차순 정렬 후 3번째 요소 출력
    print(arr[2])
