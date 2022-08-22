def solution(gems):

    n, m = len(gems), len(set(gems))
    answer = [0, n]

    l, r = 0, 0

    g_dict = {gems[0]: 1}
    while l < n and r < n:

        # 현재 범위가 모든 보석을 담았다면
        if len(g_dict) == m:
            # 현재 길이가 최소 길이라면 갱신
            if r-l < answer[1] - answer[0]:
                answer = [l, r]

            # 최소 길이가 아니라면 왼쪽을 당김
            else:
                g_dict[gems[l]] -= 1
                if g_dict[gems[l]] == 0:
                    del g_dict[gems[l]]
                l += 1


        # 모든 보석을 못담았다면 오른쪽 늘림
        else:
            r += 1
            if r == n:break

            if g_dict.get(gems[r]):
                g_dict[gems[r]] += 1
            else:
                g_dict[gems[r]] = 1

    return [answer[0]+1, answer[1]+1]

    '''
    g_dict = dict()
    n, m = 0, 0
    for gem in gems:
        m += 1
        if g_dict.get(gem):continue
        n += 1
        g_dict[gem] = True

    k = n
    while k <= m:
        for i in range(0, m-k+1):
            tmp = gems[i:i+k]
            for j in tmp:
                
            if tmp == g_dict:
                return [i+1, i+k]
        k += 1
    '''

'''

def solution(gems):
    answer = []

    arr = set(gems)
    n, m = len(gems), len(arr)

    l, r = 0, m-1

    min_cnt = n+1
    Flag = 0
    while not Flag:
        tmp = gems[l:r]
        Flag = 1
        # 현재 범위가 모든 보석을 담았다면
        if set(gems[l:r]) & arr == arr:
            Flag -= 1
            # 현재 길이가 최소 길이라면 갱신
            if r-l < min_cnt:
                min_cnt = r-l
                answer = [l+1, r]
                if min_cnt==m:
                    break
            # 최소 길이가 아니라면 왼쪽을 당김
            else:
                l += 1


        # 모든 보석을 못담았다면 오른쪽 늘림
        else:
            while r < n:
                if Flag == 1:
                    Flag -= 1
                r += 1
                if gems[r-1] not in gems[l:r-1]:
                    break
    return answer

'''
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))