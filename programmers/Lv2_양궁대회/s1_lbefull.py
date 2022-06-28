arrows = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
max_dif = 0
answer = []


def dfs(cnt, n, pre, info):
    '''
    cnt  : 화살 쏜 횟수
    n    : 총 화살
    pre  : 이전 화살 인덱스
    info : 어피치가 맞힌 과녁
    '''
    global answer, max_dif
    if cnt == n:                                                # 화살을 n번 쐈으면
        score_a = 0
        score_l = 0
        for i in range(11):                                     # 둘의 과녁 리스트를 순회하면서
            if arrows[i] > info[i]:                             # 라이언이 더 많이 맞췄으면
                score_l += 10 - i                               # 라이언에게 점수추가
            elif info[i] != 0 and arrows[i] <= info[i]:         # 1발 이상 맞췄고 어피치가 같거나 더 많이 맞췄으면
                score_a += 10 - i                               # 어피치에게 점수추가
        
        if score_l > score_a:                                   # 라이언의 점수가 클 경우
            if max_dif < (score_l - score_a):                   # 둘의 차이가 저장된 차이보다 크면
                max_dif = (score_l - score_a)                   # 갱신 후
                answer = arrows[:]                              # 정답을 현재 라이언 과녁 리스트로 바꿔줌
            
            elif max_dif == (score_l - score_a):                # 점수차이가 저장된 최고 차이랑 같으면
                for i in range(10, -1, -1):                     # 과녁의 뒤부터 비교해서
                    if arrows[i] < answer[i]:                   # 기존 과녁이 더 많이 맞췄으면
                        break                                   # 기존 결과 유지
                    if arrows[i] > answer[i]:                   # 현재 과녁이 더 많이 맞췄으면
                        answer = arrows[:]                      # 갱신
                        break

        return

    for i in range(pre, 11):                # 과녁을 맞추는 모든 경우의 수를 만들기 위한 조합
        arrows[i] += 1                      # 현재 인덱스 과녁을 맞추고
        dfs(cnt + 1, n, i, info)            # 재귀 후
        arrows[i] -= 1                      # 다시 빼줌


def solution(n, info):
    global answer
    dfs(0, n, 0, info)
    if not answer:                          # answer이 한번도 갱신되지 않았다면
        answer = [-1]                       # 라이언이 질 수 밖에 없으므로 [-1] 반환
    return answer


# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
