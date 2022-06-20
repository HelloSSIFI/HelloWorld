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
    
    stack = [(i, 1, i) for i in times]     # 입국심사가 끝나는 시간, 입국심사를 받은 횟수, 입국심사가 이뤄지는 시간
    heapq.heapify(stack)                   # 정렬

    while n:                                            # 대기하는 사람이 없을 때까지
        val, cnt, now = heapq.heappop(stack)            # 가장 빨리 끝나는 심사대

        n -= 1                                          # 사람 1명 차감
        if not n:return val                             # 남은 사람이 없다면 return
        cnt += 1                                        # 횟수 + 1

        heapq.heappush(stack, (now*cnt, cnt, now))      # 끝나는 시간을 갱신해서 heapq에 push
'''

def solution(n, times):

    l = 1                       # 최소 대기시간: 처음 입력의 최솟값
    r = max(times)*n            # 최대 대기시간: 현재 times의 최댓값 * 사람 수

    while l <= r:               # 이분 탐색의 시작과 끝이 역전될 때까지
        tmp = 0                 # 통과할 수 있는 사람 수
        mid = (l+r)//2          # 중간 대기시간 = (시작 + 끝) // 2
        for t in times:         # mid/t의 몫: 중간 대기시간으로 해당 심사대가 통과할 수 있는 사람 수
            tmp += mid//t

        if tmp >= n:            # 통과하는 사람수가 n 이상이면
            ans = mid           # n일 수 있으니 일단 ans를 갱신
            r = mid-1           # 이상일 수 있으니 끝 값 갱신

        else:                   # n 이하 통과했으니 시작점 갱신
            l = mid+1


    return ans                  # 반복문이 끝나고, ans값 return

print(solution(6, [7, 10]))
