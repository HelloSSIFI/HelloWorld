S = input()
cnt = dict()
cnt['A'] = cnt['B'] = cnt['C'] = 0
result = []
for s in S:                                                                     # 각 직원의 출근일을 카운트
    cnt[s] += 1

c_dist = 3                                                                      # 이전에 C가 출근한 날에서 얼마나 지났는지 저장
b_dist = 2                                                                      # 이전에 B가 출근한 날에서 얼마나 지났는지 저장
for _ in range(len(S)):                                                         # S의 길이만큼 새로운 문자열을 만듬
    if cnt['B'] and b_dist > 1 and (cnt['B'] > cnt['C'] or c_dist < 3):         # B의 출근이 남았고, 이전에 출근한지 1일이상 지났고, B의 출근이 C보다 더 많이 남았거나 C가 출근한지 2일 이하라면
        result.append('B')                                                      # B를 출근시키고
        cnt['B'] -= 1                                                           # B의 남은 출근일을 1 내려주고
        b_dist = 0                                                              # B의 이전 출근한 날을 0으로 갱신
    
    elif cnt['C'] and c_dist > 2 and (cnt['C'] >= cnt['B'] or b_dist < 2):      # C도 B와 마찬가지, C는 B와 출근일이 동일하게 남았을 경우 C가 먼저 출근
        result.append('C')                                                      # C를 출근히키고
        cnt['C'] -= 1                                                           # C의 남은 출근일을 1 내려주고
        c_dist = 0                                                              # C의 이전 출근한 날을 0으로 갱신
    
    elif cnt['A']:                                                              # 그 이외에 A의 출근일이 남았다면
        result.append('A')                                                      # A를 출근시키고 카운트 -1
        cnt['A'] -= 1
    
    else:                                                                       # 위의 경우가 아니라면
        result = ['-1']                                                         # 올바른 출근 기록이 없으므로 -1을 출력
        break
    
    b_dist += 1                                                                 # B와 C의 이전 출근일과의 거리를 1씩 증가
    c_dist += 1

print(''.join(result))
