from collections import defaultdict

def solution(genres, plays):
    answer = []
    genre_cnt = defaultdict(int)    # 장르: 장르에 해당하는 노래들의 재생된 횟수의 합
    check = defaultdict(list)    # 장르: [장르내 노래 재생 횟수, 고유번호]

    for i in range(len(genres)):
        genre_cnt[genres[i]] += plays[i]
        check[genres[i]].append([plays[i], i])

    genre_cnt = sorted(genre_cnt.items(), key= lambda x: (-x[1], x[0]))    # 누적된 재생횟수를 기준으로 정렬

    for genre, _ in genre_cnt:
        # 장르내에서 두 곡만 수록하기 때문에 재생횟수 기준으로 정렬 후 1 or 2곡만 가져온다.
        temp = sorted(check[genre], key=lambda x: (-x[0], x[1]))[:2]
        for val, idx in temp:    # answer에 고유번호 추가
            answer.append(idx)

    return answer