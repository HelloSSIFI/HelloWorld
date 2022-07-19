from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    for i, p in enumerate(priorities):
        q.append((i, p))

    printed = []
    while q:
        doc = q.popleft()
        flag = False
        for p in list(q):
            if p[1] > doc[1]:
                flag = True
                break
        if flag:
            q.append(doc)
        else:
            printed.append(doc)
        
    for doc in printed:
        if doc[0] == location:
            answer = printed.index(doc) + 1
            break
            
    return answer

'''
best solution 1)

def solution(priorities, location):
    answer = 0
    search, c = sorted(priorities, reverse=True), 0         # 어차피 인쇄는 우선순위 대로 출력이 되므로 우선순위가 큰 순서대로 정렬
    while True:
        for i, priority in enumerate(priorities):
            s = search[c]
            if priority == s:
                c += 1
                answer += 1
                if i == location:
                    break
        else:
            continue
        break
    return answer

'''

'''
best solution 2)

any 함수를 사용한 풀이

# any()는 인자로 iterable한 객체를 받는다.
# cur[1] < q[1] for q in queue 와 같이 comprehension을 사용하면 조건의 참/거짓 결과가 담긴 iterable한 generator가 만들어지고
# any 함수로 generator 객체를 순회하면서 True를 발견하기만 하면 곧바로 True를 return한다.(any의 기능)

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):               
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

'''

