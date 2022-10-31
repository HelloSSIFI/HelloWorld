# key point : info에 대한 해쉬맵을 생성하여 해결한다.
# 해쉬를 만들 수 있는 경우가 제한적이고, 해쉬의 각 부분이 유니크하기 때문에 가능한 방법

def solution(info, query):
    answer = []

    info_table = {}

    # 점수를 제외하고 모든 경우에 대해 해쉬 키 작성
    for lang in ['python', 'cpp', 'java', '-']:
        for position in ['backend', 'frontend', '-']:
            for skilled in ['junior', 'senior', '-']:
                for food in ['chicken', 'pizza', '-']:
                    info_table[lang + position + skilled + food] = []
 
    for detail in info:
        # lang, position, skilled, food, score = detail.split()
        d = detail.split()
        for lang in [d[0], '-']:
            for position in [d[1], '-']:
                for skilled in [d[2], '-']:
                    for food in [d[3], '-']:
                        info_table[lang + position + skilled + food].append(int(d[4]))

    # 각각의 해쉬 키에 저장된 점수에 대해서 오름차순 정렬
    for key in info_table.keys():
        if info_table[key]:
            info_table[key].sort()

    # query를 해쉬키로 만들고, 해당 해쉬키에 저장된 점수 중 query의 점수 이상인 것의 개수 count
    for q in query:
        q = q.replace(' and ', '')
        hash_key, score = q.split()
        score = int(score)

        if not info_table[hash_key]:
            answer.append(0)
            continue

        scores_info = info_table[hash_key]
        length = len(scores_info)
        temp = length

        left = 0
        right = length - 1
        while left <= right:
            mid = (left + right) // 2

            if scores_info[mid] >= score:
                temp = mid
                right = mid - 1
            else:
                left = mid + 1
        
        answer.append(length - temp)

    return answer




## 효율성 테스트 통과 실패

# from collections import defaultdict

# def search(req, sorted_keys, db):
#     lang, position, skilled, food_and_score = list(map(lambda x : x.strip(), req.split('and')))
#     food, score = food_and_score.split()
    
#     left = 0
#     right = len(sorted_keys) - 1
    
#     if db[sorted_keys[right]][4] < int(score):
#         return 0
    
#     while left <= right:
#         mid = (left + right) // 2
#         score_idx = sorted_keys[mid]
        
#         if db[score_idx][4] >= int(score):
#             right = mid - 1
#         else:
#             left = mid + 1
            
#     group = sorted_keys[left:]
#     cnt = 0
#     for row in group:
#         if (lang == '-' or lang in db[row]) and (position == '-' or position in db[row]) and (skilled == '-' or skilled in db[row]) and (food == '-' or food in db[row]):
#             cnt += 1

#     return cnt


# def solution(info, query):
#     answer = []
#     db = defaultdict(list)
#     for i in range(1, len(info) + 1):
#         db[i] = info[i - 1].split()
#         db[i][4] = int(db[i][4])
#     sorted_keys = sorted(list(db.keys()), key=lambda x : db[x][4])
    
#     for req in query:
#         result = search(req, sorted_keys, db)
#         answer.append(result)
#     return answer
