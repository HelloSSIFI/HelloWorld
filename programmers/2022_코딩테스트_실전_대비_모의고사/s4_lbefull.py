import copy


def solution(beginning, target):
    global N, M
    N = len(beginning)
    M = len(beginning[0])
    answer = 1000
    beginning_copy = copy.deepcopy(beginning)


    def turn(idx, d):                                                   # 동전을 한 줄 뒤집는 함수
        if d == 0:                                                      # d가 0이라면 idx행을 뒤집고
            for c in range(M):                                          # d가 1이라면 idx열을 뒤집음
                beginning[idx][c] = (beginning[idx][c] + 1) % 2
        else:
            for r in range(N):
                beginning[r][idx] = (beginning[r][idx] + 1) % 2

    
    def check():                                                        # beginning과 target이 같은지 확인하는 함수
        for r in range(N):
            for c in range(M):
                if beginning[r][c] != target[r][c]:
                    return False
        return True


    def find_target(cnt):                                               # 첫 번째 행에 맞도록
        for c in range(M):                                              # 모든 열을 뒤집은 후
            if beginning[0][c] != target[0][c]:                         # 두번째 행부터 각행을 확인하면서
                cnt += 1                                                # target과 다르다면 뒤집어줌
                turn(c, 1)                                              # 각 행과 열은 한번씩만 뒤집고 뒤집은 횟수를 반환

        for r in range(1, N):
            for c in range(M):
                if beginning[r][c] != target[r][c]:
                    cnt += 1
                    turn(r, 0)
                    break
        return cnt


    flag = False                                        # 첫 행을 안뒤집고
    cnt = find_target(0)                                # find_target방식으로 동전을 뒤집었을 때
    if check():                                         # target이 된다면
        flag = True                                     # answer를 cnt로 갱신
        answer = cnt
    
    beginning = copy.deepcopy(beginning_copy)           # 첫 행을 뒤집고
    turn(0, 0)                                          # find_target방식으로 동전을 뒤집었을 때
    cnt = find_target(1)                                # target이 된다면
    if check():                                         # answer를 cnt와 비교해서 작은것을 넣어줌
        flag = True
        answer = min(answer, cnt)
    
    if not flag:                                        # 둘 다 target이 될 수 없다면
        return -1                                       # -1 반환
    return answer


# print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[1, 0, 1], [0, 0, 0], [0, 0, 0]]))
