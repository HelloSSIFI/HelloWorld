'''
def solution(n, times):

    stack = [(i, 1, i) for i in times]     # 시간과 곱할 수

    stack.sort(key=lambda x:x[0])

    while n:

        val, cnt, now = stack[0]

        n -= 1
        if not n:return val
        cnt += 1

        stack[0] = ((now*cnt, cnt, now))
        stack.sort(key=lambda x:x[0])



import heapq


def solution(n, times):
    
    stack = [(i, 1, i) for i in times]     # 시간과 곱할 수
    heapq.heapify(stack)                # 정렬

    while n:
        val, cnt, now = heapq.heappop(stack)

        n -= 1
        if not n:return val
        cnt += 1

        heapq.heappush(stack, (now*cnt, cnt, now))
'''

def solution(n, times):

    l = 1
    r = max(times)*n

    while l <= r:
        tmp = 0
        mid = (l+r)//2
        for t in times:
            tmp += mid//t

        if tmp >= n:
            ans = mid
            r = mid-1

        else:
            l = mid+1


    return ans

print(solution(6, [7, 10]))
