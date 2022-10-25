from collections import Counter


def solution(a):
    answer = -1
    num_cnt = Counter(a)

    for num in num_cnt:
        if num_cnt[num] <= answer:    # 스타수열의 공통원소의 개수가 answer보다 작으면 더이상 확인할 필요가 없다.
            continue

        cnt = 0
        idx = 0
        while idx < len(a)-1:
            # 공통된 num값이 없는 경우 / 각 집합내 숫자가 다르다는 조건을 만족하지 않는 경우
            if a[idx] != num != a[idx+1] or a[idx] == a[idx+1]:
                idx += 1
                continue

            cnt += 1    # 원소 사용 횟수 +1
            idx += 2    # 다음 배열 탐색

        answer = max(answer, cnt)

    if answer == -1:
        return 0
    return answer * 2