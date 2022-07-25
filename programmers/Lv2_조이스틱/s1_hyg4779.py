from collections import deque

def solution(name):
    answer = float('inf')
    N = len(name)
    result = [0]*N
    for i in range(N):
        result[i] = 0 if name[i]=='A' else min(91-ord(name[i]), ord(name[i])-65)

    tmp = result[0]
    result[0] = 0
    Q = deque([(0, tmp, result)])       # 현재 위치, 버튼 횟수, 현재 배열
    while Q:
        idx, cnt, now = Q.popleft()

        if sum(now)==0:
            answer = min(answer, cnt)
            continue

        j = 1
        while j < N//2+1:
            p, m = (idx+j)%N, (idx-j)%N
            if now[p]:
                tmp = now[p]
                now[p] = 0
                Q.append((p, cnt+j+tmp, now[:]))
                now[p] = tmp

            if now[m]:
                tmp = now[m]
                now[m] = 0
                Q.append((m, cnt+j+tmp, now[:]))
                now[m] = tmp
            j+=1

    return answer


print(solution("JEROEN"))
print(solution("JAN"))
