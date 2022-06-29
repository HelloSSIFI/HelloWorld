import copy

max_score_diff = 0
answer = []

def cal_score(apeach_shot, ryan_shot):
    apeach_score = 0
    ryan_score = 0

    for i in range(11):
        # 둘 다 0점 일 경우
        if (apeach_shot[i], ryan_shot[i]) == (0, 0):
            continue
        # 어피치가 점수가 크거나 같을 경우
        if apeach_shot[i] >= ryan_shot[i]:
            apeach_score += (10 - i)
        # 라이언이 높을 경우
        else:
            ryan_score += (10 - i)

    return ryan_score - apeach_score


def dfs(apeach_shot, ryan_shot, n, idx):
    global max_score_diff, answer

    # idx가 0점까지 도달했을 때
    if idx == 11:
        # 화살이 남은 경우
        if n != 0:
            ryan_shot[10] = n    # 모두 가장 낮은 점수에 몰아주기
        score_diff = cal_score(apeach_shot, ryan_shot)    # 어피치와 스코어 비교

        # 스코어차가 음수이면 어피치가 높다는 것이므로 리턴
        if score_diff <= 0:
            return
        # 아닐경우 라이언의 기록 임시저장
        temp = copy.deepcopy(ryan_shot)

        # 어피치와의 스코어 차이가 최대 차이 보다 클 경우
        if score_diff > max_score_diff:
            max_score_diff = score_diff    # 최고 점수 변경
            answer = [temp]    # 최고 기록 덮어쓰기
            return

        # 같은 경우
        if score_diff == max_score_diff:
            answer.append(temp)    # 기록 추가

        return

    # 해당 점수(idx)에서 점수를 획득 했을 때
    if apeach_shot[idx] < n:
        ryan_shot.append(apeach_shot[idx]+1)
        dfs(apeach_shot, ryan_shot, n-apeach_shot[idx]-1, idx+1)
        ryan_shot.pop()

    # 해당 점수(idx)에서 점수를 획득 하지 못했을 때
    ryan_shot.append(0)
    dfs(apeach_shot, ryan_shot, n, idx+1)
    ryan_shot.pop()



def solution(n, info):
    global answer

    dfs(info, [], n, 0)

    if answer == []:
        return [-1]

    # 작은 수로 하는 것을 리턴해야 하기 때문에 정렬 후 0번 째 인덱스 결과값 리턴
    answer.sort(key=lambda x : x[::-1], reverse=True)

    return answer[0]