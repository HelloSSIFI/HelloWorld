from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = deque()
    time = 0
    cities = list(map(lambda x : x.upper(), cities))
    for city in cities:
        if cacheSize == 0:
            time += 5
            continue

        if len(q) < cacheSize and city not in q:
            q.append(city)
            time += 5
            continue

        if city in q:
            here = q.index(city)
            list_q = list(q)
            temp = list_q[ :here] + list_q[here + 1:] + [city]
            print('temp: ', temp)
            q = deque(temp)
            time += 1
        else:
            q.popleft()
            q.append(city)
            time += 5
    answer = time
    return answer

# print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
# print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(3, ["Jeju", "jeju", "jeju", "seoul", "jeju"]))

