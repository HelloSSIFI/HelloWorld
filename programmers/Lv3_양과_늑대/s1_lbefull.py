pos = set()                                     # 현재 갈 수 있는 늑대 노드를 저장

def sheep_find(v):                              # 갈 수 있는 늑대노드를 추가해주고 양의 수를 반환
    cnt = 0
    for edge in line[v]:                        # 현재 노드에서 갈 수 있는 노드 탐색
        if not inform[edge]:                    # 양 노드이면
            cnt += 1                            # cnt +1
            cnt += sheep_find(edge)             # 해당 노드를 방문(재귀)하면서 반환되는 cnt를 모두 더해줌

        else:                                   # 늑대 노드이면
            pos.add(edge)                       # pos에 추가
    
    return cnt                                  # 방문 가능한 양 노드의 수를 리턴


def find(v, sheep_cnt, wolf_cnt):
    '''
    v         : 현재 정점
    sheep_cnt : 현재 따라오는 양 수
    wolf_cnt  : 현재 따라오는 늑대 수
    '''
    global answer, pos
    if sheep_cnt <= wolf_cnt:                   # 늑대의 수가 양의 수 이상이면 리턴
        return
    
    init_pos = pos.copy()                       # 현재 갈 수 있는 늑대 노드를 복사

    sheep_cnt += sheep_find(v)                  # 현재 갈 수 있는 양 노드를 모두 돌면서 양의 수를 추가해주고 늑대 노드를 추가해줌
    answer = max(answer, sheep_cnt)             # answer 갱신

    cur_pos = pos.copy()                        # 반복을 돌기위해 현재 pos 셋을 복사

    for el in cur_pos:
        pos.remove(el)                          # 방문할 노드를 pos에서 지워주고
        find(el, sheep_cnt, wolf_cnt + 1)       # 늑대의 수를 1증가 후 방문(재귀)
        pos.add(el)                             # 다시 pos에 노드 추가
    
    pos = init_pos                              # 재귀가 끝나기 전에 처음에 복사한 init_pos로 노드 정보를 되돌림


def solution(info, edges):
    global line, answer, inform
    inform = info
    answer = 0
    line = [[] for _ in range(len(info))]
    for s, e in edges:                          # 트리 정보 저장
        line[s].append(e)
    
    find(0, 1, 0)
    return answer


# print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))
