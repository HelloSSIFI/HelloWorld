def solution(cacheSize, cities):
    if cacheSize == 0:                              # 캐시 크기가 0 이면
        return 5 * len(cities)                      # 각 처리당 실행시간 5 이므로 곱해서 리턴

    answer = 0
    cache = dict()                                  # 캐시를 딕셔너리로 선언
    cnt = 0                                         # 캐시에 표시할 우선순위
    for city in cities:                             # 도시를 순회
        cnt += 1                                    # 우선순위 +1
        if city.lower() in cache:                   # 캐시에 도시가 있으며
            answer += 1                             # 실행시간 1 추가
            cache[city.lower()] = cnt               # 캐시에서 현재 도시의 우선순위를 갱신해줌
            continue

        answer += 5                                 # 캐시에 없다면 실행시간 5 추가
        if len(cache) == cacheSize:                 # 캐시가 꽉 찼으면
            min_key = min(cache, key=cache.get)     # 우선순위가 제일 낮은것을 삭제
            cache.pop(min_key)
        cache[city.lower()] = cnt                   # 현재 도시를 현재 우선순위로 넣어줌

    return answer

# print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
