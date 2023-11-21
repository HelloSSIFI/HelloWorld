def solution(n, cores):
    if n <= len(cores):    # 작업량 보다 코어 수가 더 큰 경우
        return n

    n -= len(cores)    # 모든 코어에 작업 할당
    l, r = 1, max(cores) * n    # l: 최소 시간, r: 최대 시간
    while l < r:    # 이진 탐색을 통해 작업 소요 시간을 구함
        mid = (l+r) // 2
        temp = 0
        for core in cores:
            temp += mid // core

        if temp >= n:
            r = mid
        else:
            l = mid + 1

    n -= sum(map(lambda x: (r-1) // x, cores))    # 작업 완료 한시간 전 작업 할당 후 남은 작업량 체크

    for i in range(len(cores)):    # 작업 완료 시간에 마지막 작업을 처리하는 코어 번호를 찾는다
        if r % cores[i] == 0:
            n -= 1
            if n == 0:
                return i + 1