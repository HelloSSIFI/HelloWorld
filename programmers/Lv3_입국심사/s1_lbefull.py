answer = 0

def search(l, r, n, times):
    global answer
    if l > r:                           # 최소값이 최대값보다 커지면
        answer = l                      # 정답을 최소값으로 설정 후 리턴
        return
    
    m = (l + r) // 2                    # 중간값
    cnt = 0

    for i in range(len(times)):         # 중간값으로 심사 가능한 인원을 구함
        cnt += m // times[i]
    
    if cnt < n:                         # 인원이 n보다 작으면
        search(m + 1, r, n, times)      # 중간값+1 ~ r 구간으로 다시 재귀
    
    else:                               # 인원이 n보다 크거나 같으면
        search(l, m - 1, n, times)      # l ~ 중간값-1 구간으로 다시 재귀


def solution(n, times):
    search(0, n * max(times), n, times)
    return answer


# print(solution(6, [7, 10]))
