def solution(cards):
    group = set()
    for i in range(len(cards)):
        visited = set([i])                                  # 상자 그룹을 저장
        j = cards[i] - 1
        while j not in visited:                             # 열린 상자가 나올때까지 그룹에 추가
            visited.add(j)
            j = cards[j] - 1
        group.add(tuple(sorted(visited)))                   # 그룹을 정렬하여 중복제거

    group = sorted(group, key=lambda x: -len(x))            # 길이가 긴 순서대로 정렬
    group.append([])                                        # 한개일 경우 0점을 만들어줄 빈 리스트 추가
    return len(group[0]) * len(group[1])                    # 긴 리스트 두 개를 곱해서 반환


# print(solution([8, 6, 3, 7, 2, 5, 1, 4]))
