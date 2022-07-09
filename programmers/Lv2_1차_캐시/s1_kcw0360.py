from collections import deque

def solution(cacheSize, cities):
    answer = 0
    memory = deque()

    if cacheSize == 0:
        return len(cities) * 5
    else:
        for city in cities:
            city = city.lower()

            if city in memory:
                answer += 1
                memory.remove(city)
                memory.append(city)
            else:
                if len(memory) == cacheSize:
                    memory.popleft()
                answer += 5
                memory.append(city)

    return answer

