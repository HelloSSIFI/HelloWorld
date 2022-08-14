import sys
input = sys.stdin.readline


N = int(input())
words = [input().rstrip() for _ in range(N)]
words.sort(key=lambda x: len(x))    # 길이순으로 정렬

answer = 0
for i in range(len(words)):
    flag = True    # 접두어 판별 후 True이면 부분집합 가능원소로 카운트
    length_a = len(words[i])

    for j in range(i+1, len(words)):    # 접두어 비교
        if words[i] == words[j][:length_a]:    # 접두어가 되는 경우 부분집합 포함 불가
            flag = False
            break    # 반복문 빠져나가기

    if flag:
        answer += 1

print(answer)



