
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
def solution(n, times):
    '''
    n: 심사받아야 하는 사람 수
    times: 심사관들의 심사 시간
    '''
    answer = 0

    left = 0
    right = max(times) * max(times)
    answer = right
    while left <= right:
        people = 0
        mid = (left + right) // 2

        for time in times:
            people += (mid // time)
            if people >= n:
                break

        if people >= n:
            answer = mid        
            right = mid - 1

        elif people < n:
            left = mid + 1


    return answer
print(solution(6, [7, 10]))
