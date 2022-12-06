def get_perms(k, perms = []):                                       # 우박수열 구하기
    perms.append(k)
    
    if k == 1:
        return perms
    
    if k % 2:
        return get_perms(k * 3 + 1, perms)
    else:
        return get_perms(k // 2, perms)

def solution(k, ranges):
    answer = []
    perms = get_perms(k)
    total_area = []                                                 # 구간 별 면적 구하기
    for s in range(len(perms) - 1):
        e = s + 1
        vertical_len = max(perms[s], perms[e])
        area = vertical_len - (abs(perms[e] - perms[s]) / 2)
        total_area.append(area)

    for rang in ranges:                                             # 범위 면적 구하기
        s, e = rang[0], len(perms) - 1 + rang[1]
        if s == e:
            answer.append(0.0)
            continue
        if s > e:
            answer.append(-1.0)
            continue
        answer.append(sum(total_area[s : e]))
        
    return answer