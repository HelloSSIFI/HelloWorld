from collections import deque

def solution(cacheSize, cities):
    answer = 0
    db = deque()

    if cacheSize == 0:    # 캐시 크기가 0이면 저장 불가능
        return len(cities) * 5
    else:
        for city in cities:
            city = city.lower()    # 대소문자 구분없게 하기 위해 소문자로 통일

            if city in db:    # DB에 존재하는 도시일 경우
                answer += 1    # hit일 경우 실행시간 추가
                db.remove(city)    # 캐시 교체 알고리즘(LRU) 적용
                db.append(city)    # 해당 도시를 제거 후 재기록
            else:    # DB에 존재하지 않는 도시일 경우
                if len(db) == cacheSize:    # DB 캐시의 크기가 최대인 경우
                    db.popleft()    # 가장 오래된 것을 삭제
                answer += 5    # miss일 경우 실행시간 추가
                db.append(city)    # DB캐시에 도시 이름 추가

    return answer

