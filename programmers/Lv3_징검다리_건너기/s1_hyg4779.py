# Binary Search
def solution(stones, k):
    l, r = 1, max(stones)

    while l <= r:
        mid = (l + r)//2

        # 건너뛰기
        cnt = 0

        for stone in stones:
            '''
            돌은 빠른 것부터 건너기 때문에 먼저 마주한 돌은 모두가 건넌다
            > 해당 돌이 0이하면 점프
            > 점프한 돌이 k개를 넘으면 못 건넌다
            '''
            if stone - mid <= 0:
                cnt += 1

                if cnt >= k:
                    r = mid - 1
                    break
            else:
                cnt = 0

        else:
            l = mid + 1

    return l

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))