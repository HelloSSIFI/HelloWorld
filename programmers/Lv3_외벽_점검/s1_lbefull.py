from itertools import permutations


def solution(n, weak, dist):
    def chk(selected):
        for i in range(m):                              # weak의 각 지점에서 입력받은 순열대로 점검을 진행
            p = weak[i]
            j = i
            cnt = 0
            for k in selected:                          # 순열에서 점검 가능한 거리 k를 받아옴
                p += k                                  # 외벽 좌표 p에서 k만큼 이동하여 점검진행
                while cnt < m and p >= weak[j]:         # waek에서 진행된 개수만큼 cnt에 체크
                    cnt += 1
                    j += 1
                    if j == m:
                        j = 0
                        p -= n

                if cnt == m: return True                # 모든 weak의 지점을 점검하였다면 True를 반환
                p = weak[j]                             # 아니라면 다음 지점을 p로 저장하고 다음 점검 진행

        return False                                    # 모든 친구들이 점검을 마쳐도 모든 weak를 점검하지 못하면 False를 반환


    m = len(weak)
    for i in range(1, len(dist) + 1):
        for j in permutations(dist, i):                 # dist에서 i명을 뽑아서 순열 j를 만듬
            if chk(j): return i                         # 해당 순열 j로 외벽 점검이 가능한지 chk함수를 실행하여 점검 가능하면 인원수 i가 정답
    return -1                                           # 어떻게 해도 점검이 불가능하면 -1


# print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
